# Pybind11 高级教程

## 目录

1. [NumPy 集成](#numpy-集成)
2. [多线程与 GIL](#多线程与-gil)
3. [模板和泛型编程](#模板和泛型编程)
4. [自定义类型转换](#自定义类型转换)
5. [异常处理](#异常处理)
6. [内存管理](#内存管理)
7. [性能优化技巧](#性能优化技巧)
8. [调试技巧](#调试技巧)

---

## NumPy 集成

### 基本 NumPy 数组绑定

```cpp
#include <pybind11/numpy.h>

// 接受 NumPy 数组
py::array_t<double> process_array(py::array_t<double> input) {
    // 获取数组信息
    auto buf = input.request();
    double *ptr = static_cast<double *>(buf.ptr);
    size_t size = buf.size;
    
    // 处理数据
    for (size_t i = 0; i < size; i++) {
        ptr[i] *= 2.0;
    }
    
    return input;
}

// 绑定
m.def("process_array", &process_array, "处理 NumPy 数组");
```

### 带形状检查的 NumPy 数组

```cpp
py::array_t<double> matrix_multiply(
    py::array_t<double> a,
    py::array_t<double> b
) {
    auto buf_a = a.request();
    auto buf_b = b.request();
    
    // 检查维度
    if (buf_a.ndim != 2 || buf_b.ndim != 2) {
        throw std::runtime_error("输入必须是 2D 数组");
    }
    
    // 检查形状
    if (buf_a.shape[1] != buf_b.shape[0]) {
        throw std::runtime_error("矩阵维度不匹配");
    }
    
    size_t rows = buf_a.shape[0];
    size_t cols = buf_b.shape[1];
    size_t inner = buf_a.shape[1];
    
    // 创建输出数组
    auto result = py::array_t<double>({rows, cols});
    auto buf_result = result.request();
    
    double *ptr_a = static_cast<double *>(buf_a.ptr);
    double *ptr_b = static_cast<double *>(buf_b.ptr);
    double *ptr_result = static_cast<double *>(buf_result.ptr);
    
    // 矩阵乘法
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) {
            ptr_result[i * cols + j] = 0;
            for (size_t k = 0; k < inner; k++) {
                ptr_result[i * cols + j] += 
                    ptr_a[i * inner + k] * ptr_b[k * cols + j];
            }
        }
    }
    
    return result;
}
```

---

## 多线程与 GIL

### 释放 GIL

```cpp
#include <pybind11/pybind11.h>
#include <thread>
#include <chrono>

// 长时间运行的计算，释放 GIL
void long_running_computation(int iterations) {
    py::gil_scoped_release release;  // 释放 GIL
    
    for (int i = 0; i < iterations; i++) {
        // 执行计算...
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
    
    // GIL 在作用域结束时自动重新获取
}

// 绑定（自动释放 GIL）
m.def("long_running_computation", &long_running_computation,
      py::call_guard<py::gil_scoped_release>());
```

### 多线程安全

```cpp
#include <mutex>

class ThreadSafeCounter {
private:
    mutable std::mutex mtx_;
    int count_ = 0;
    
public:
    void increment() {
        std::lock_guard<std::mutex> lock(mtx_);
        count_++;
    }
    
    int get() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return count_;
    }
};

// 绑定
py::class_<ThreadSafeCounter>(m, "ThreadSafeCounter")
    .def(py::init<>())
    .def("increment", &ThreadSafeCounter::increment,
         py::call_guard<py::gil_scoped_release>())
    .def("get", &ThreadSafeCounter::get);
```

---

## 模板和泛型编程

### 模板函数绑定

```cpp
// C++ 模板函数
template<typename T>
T add(T a, T b) {
    return a + b;
}

// 绑定多个特化版本
m.def("add", &add<int>, "整数加法");
m.def("add", &add<double>, "浮点数加法");
m.def("add", &add<std::string>, "字符串连接");
```

### 模板类绑定

```cpp
template<typename T>
class Vector {
private:
    std::vector<T> data_;
    
public:
    void push_back(const T& value) {
        data_.push_back(value);
    }
    
    T get(size_t index) const {
        return data_[index];
    }
    
    size_t size() const {
        return data_.size();
    }
};

// 绑定特化版本
using IntVector = Vector<int>;
using DoubleVector = Vector<double>;

py::class_<IntVector>(m, "IntVector")
    .def(py::init<>())
    .def("push_back", &IntVector::push_back)
    .def("get", &IntVector::get)
    .def("size", &IntVector::size);

py::class_<DoubleVector>(m, "DoubleVector")
    .def(py::init<>())
    .def("push_back", &DoubleVector::push_back)
    .def("get", &DoubleVector::get)
    .def("size", &DoubleVector::size);
```

---

## 自定义类型转换

### 自定义类型到 Python

```cpp
struct Point {
    double x, y;
    
    std::string __repr__() const {
        return "Point(" + std::to_string(x) + ", " + std::to_string(y) + ")";
    }
};

// 类型转换器
namespace pybind11 {
    template <>
    struct type_caster<Point> {
    public:
        PYBIND11_TYPE_CASTER(Point, _("Point"));
        
        bool load(handle src, bool convert) {
            if (!src) return false;
            if (!convert && !py::isinstance<py::dict>(src)) return false;
            
            auto d = py::cast<py::dict>(src);
            if (!d.contains("x") || !d.contains("y")) return false;
            
            value.x = py::cast<double>(d["x"]);
            value.y = py::cast<double>(d["y"]);
            return true;
        }
        
        static handle cast(const Point& src, return_value_policy, handle) {
            py::dict d;
            d["x"] = src.x;
            d["y"] = src.y;
            return d.release();
        }
    };
}

// 使用
m.def("distance", [](const Point& p1, const Point& p2) {
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;
    return std::sqrt(dx * dx + dy * dy);
});
```

---

## 异常处理

### 注册自定义异常

```cpp
// 定义 C++ 异常
class CustomException : public std::exception {
private:
    std::string message_;
    
public:
    CustomException(const std::string& msg) : message_(msg) {}
    const char* what() const noexcept override {
        return message_.c_str();
    }
};

// 注册为 Python 异常
PYBIND11_MODULE(module, m) {
    static py::exception<CustomException> exc(m, "CustomException");
    py::register_exception_translator([](std::exception_ptr p) {
        try {
            if (p) std::rethrow_exception(p);
        } catch (const CustomException& e) {
            exc(e.what());
        }
    });
    
    // 使用
    m.def("throw_custom", []() {
        throw CustomException("自定义错误消息");
    });
}
```

### 异常转换

```cpp
// 将 C++ 异常转换为 Python 异常
m.def("divide", [](double a, double b) {
    if (b == 0.0) {
        throw std::runtime_error("除零错误");
    }
    return a / b;
});
```

---

## 内存管理

### 智能指针

```cpp
#include <memory>

class Resource {
public:
    Resource(int id) : id_(id) {}
    int get_id() const { return id_; }
private:
    int id_;
};

// 使用 shared_ptr
using ResourcePtr = std::shared_ptr<Resource>;

py::class_<Resource, ResourcePtr>(m, "Resource")
    .def(py::init<int>())
    .def("get_id", &Resource::get_id);

// 工厂函数返回 shared_ptr
m.def("create_resource", [](int id) {
    return std::make_shared<Resource>(id);
});
```

### 返回策略

```cpp
class Data {
public:
    std::string value;
};

// 不同的返回策略
py::class_<Data>(m, "Data")
    .def(py::init<>())
    .def("get_value", &Data::value,
         py::return_value_policy::reference_internal)  // 引用，不拷贝
    .def("copy_value", &Data::value,
         py::return_value_policy::copy);  // 拷贝
```

---

## 性能优化技巧

### 1. 避免不必要的拷贝

```cpp
// 使用 const 引用
double sum(const std::vector<double>& numbers) {
    // 不拷贝，直接使用引用
    return std::accumulate(numbers.begin(), numbers.end(), 0.0);
}
```

### 2. 使用移动语义

```cpp
std::vector<int> process_data(std::vector<int>&& data) {
    // 移动语义，避免拷贝
    std::sort(data.begin(), data.end());
    return std::move(data);
}
```

### 3. 内联函数

```cpp
inline double fast_add(double a, double b) {
    return a + b;
}
```

### 4. 预分配内存

```cpp
std::vector<double> generate_large_array(size_t size) {
    std::vector<double> result;
    result.reserve(size);  // 预分配
    for (size_t i = 0; i < size; i++) {
        result.push_back(i * 0.1);
    }
    return result;
}
```

---

## 调试技巧

### 1. 启用调试符号

```cmake
# CMakeLists.txt
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
```

### 2. 使用 GDB

```bash
# 编译 Debug 版本
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .

# 使用 GDB
gdb python
(gdb) run tests/test_calculator.py
(gdb) break calculator.cpp:25
(gdb) continue
(gdb) print value
```

### 3. 打印调试信息

```cpp
#include <iostream>

void debug_function() {
    std::cout << "调试信息: 进入函数" << std::endl;
    // ...
}
```

### 4. Python 端调试

```python
import calculator
import pdb

pdb.set_trace()  # 设置断点
result = calculator.add(2, 3)
```

### 5. 使用 Valgrind（内存检查）

```bash
valgrind --leak-check=full python tests/test_calculator.py
```

---

## 最佳实践总结

1. **性能优先**：使用 const 引用、移动语义、避免不必要的拷贝
2. **线程安全**：在长时间运行的操作中释放 GIL
3. **错误处理**：使用标准异常，提供清晰的错误消息
4. **内存管理**：使用智能指针，注意返回策略
5. **类型安全**：充分利用 C++ 的类型系统
6. **文档完善**：为所有函数和类添加文档字符串
7. **测试充分**：编写单元测试和集成测试

---

## 进一步学习

- [Pybind11 官方文档](https://pybind11.readthedocs.io/)
- [NumPy C API](https://numpy.org/doc/stable/reference/c-api/)
- [Python C API](https://docs.python.org/3/c-api/)
- [C++ 最佳实践](https://isocpp.github.io/CppCoreGuidelines/)

