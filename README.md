# Pybind11 C++ 打包为 Python 全面教学指南

## 📚 目录

1. [简介](#简介)
2. [环境准备](#环境准备)
3. [项目结构](#项目结构)
4. [核心概念](#核心概念)
5. [详细教程](#详细教程)
6. [高级特性](#高级特性)
7. [构建与打包](#构建与打包)
8. [最佳实践](#最佳实践)
9. [常见问题](#常见问题)

---

## 简介

Pybind11 是一个轻量级的 C++ 库，用于将 C++ 代码暴露给 Python。它是 Boost.Python 的现代替代品，具有以下优势：

- ✅ **轻量级**：仅需头文件，无需编译库
- ✅ **C++11 标准**：充分利用现代 C++ 特性
- ✅ **类型安全**：编译时类型检查
- ✅ **性能优异**：几乎零开销
- ✅ **易于使用**：简洁的 API

---

## 环境准备

### 系统要求

- **C++ 编译器**：支持 C++11 或更高版本（GCC 4.8+, Clang 3.3+, MSVC 2015+）
- **Python**：3.6 或更高版本
- **CMake**：3.4 或更高版本（推荐 3.12+）
- **pip**：用于安装 pybind11

### 安装步骤

#### 1. 安装 pybind11

```bash
# 方法 1：使用 pip（推荐）
pip install pybind11

# 方法 2：使用 conda
conda install -c conda-forge pybind11

# 方法 3：从源码安装
git clone https://github.com/pybind/pybind11.git
cd pybind11
pip install .
```

#### 2. 验证安装

```bash
python -c "import pybind11; print(pybind11.__version__)"
```

---

## 项目结构

```
py-binding/
├── README.md              # 本教学文档
├── CMakeLists.txt         # CMake 构建配置
├── setup.py              # Python setuptools 配置
├── requirements.txt       # Python 依赖
├── .gitignore            # Git 忽略文件
├── include/              # C++ 头文件
│   └── calculator.h
├── src/                  # C++ 源文件
│   └── calculator.cpp
├── python/               # Python 绑定代码
│   └── bindings.cpp
├── tests/                # Python 测试代码
│   └── test_calculator.py
└── examples/             # 使用示例
    └── example_usage.py
```

---

## 核心概念

### 1. 基本绑定流程

```
C++ 代码 → pybind11 绑定 → Python 模块 → Python 调用
```

### 2. 关键组件

- **PYBIND11_MODULE**：定义 Python 模块的宏
- **py::module_**：Python 模块对象
- **py::class_**：绑定 C++ 类
- **py::def**：绑定函数
- **类型转换**：自动处理 C++ 和 Python 类型转换

### 3. 类型映射

| C++ 类型 | Python 类型 |
|---------|------------|
| `int` | `int` |
| `float` | `float` |
| `double` | `float` |
| `std::string` | `str` |
| `std::vector<T>` | `list` |
| `std::map<K, V>` | `dict` |
| `std::tuple<...>` | `tuple` |

---

## 详细教程

### 第一步：编写 C++ 代码

#### 1.1 创建头文件（include/calculator.h）

```cpp
#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <string>
#include <vector>

class Calculator {
public:
    Calculator();
    Calculator(double initial_value);
    
    // 基本运算
    double add(double a, double b);
    double subtract(double a, double b);
    double multiply(double a, double b);
    double divide(double a, double b);
    
    // 成员变量操作
    void set_value(double value);
    double get_value() const;
    
    // 批量操作
    double sum(const std::vector<double>& numbers);
    double average(const std::vector<double>& numbers);
    
    // 静态方法
    static double power(double base, double exponent);
    
    // 字符串操作示例
    std::string greet(const std::string& name);
    
private:
    double value_;
};

// 自由函数示例
double compute_area(double radius);
std::vector<int> generate_fibonacci(int n);

#endif // CALCULATOR_H
```

#### 1.2 实现 C++ 代码（src/calculator.cpp）

```cpp
#include "calculator.h"
#include <numeric>
#include <cmath>
#include <algorithm>

Calculator::Calculator() : value_(0.0) {}

Calculator::Calculator(double initial_value) : value_(initial_value) {}

double Calculator::add(double a, double b) {
    return a + b;
}

double Calculator::subtract(double a, double b) {
    return a - b;
}

double Calculator::multiply(double a, double b) {
    return a * b;
}

double Calculator::divide(double a, double b) {
    if (b == 0.0) {
        throw std::runtime_error("Division by zero!");
    }
    return a / b;
}

void Calculator::set_value(double value) {
    value_ = value;
}

double Calculator::get_value() const {
    return value_;
}

double Calculator::sum(const std::vector<double>& numbers) {
    return std::accumulate(numbers.begin(), numbers.end(), 0.0);
}

double Calculator::average(const std::vector<double>& numbers) {
    if (numbers.empty()) {
        throw std::runtime_error("Cannot compute average of empty vector");
    }
    return sum(numbers) / numbers.size();
}

double Calculator::power(double base, double exponent) {
    return std::pow(base, exponent);
}

std::string Calculator::greet(const std::string& name) {
    return "Hello, " + name + "! Welcome to Pybind11!";
}

// 自由函数实现
double compute_area(double radius) {
    return 3.141592653589793 * radius * radius;
}

std::vector<int> generate_fibonacci(int n) {
    if (n <= 0) return {};
    if (n == 1) return {0};
    if (n == 2) return {0, 1};
    
    std::vector<int> fib = {0, 1};
    for (int i = 2; i < n; ++i) {
        fib.push_back(fib[i-1] + fib[i-2]);
    }
    return fib;
}
```

### 第二步：创建 Python 绑定

#### 2.1 编写绑定代码（python/bindings.cpp）

```cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // 用于 STL 容器转换
#include "../include/calculator.h"

namespace py = pybind11;

// 定义 Python 模块
PYBIND11_MODULE(calculator, m) {
    m.doc() = "Pybind11 示例：计算器模块";
    
    // ========== 绑定类 ==========
    py::class_<Calculator>(m, "Calculator")
        // 构造函数
        .def(py::init<>())
        .def(py::init<double>(), "构造函数，设置初始值", py::arg("initial_value") = 0.0)
        
        // 基本运算方法
        .def("add", &Calculator::add, "加法运算", 
             py::arg("a"), py::arg("b"))
        .def("subtract", &Calculator::subtract, "减法运算",
             py::arg("a"), py::arg("b"))
        .def("multiply", &Calculator::multiply, "乘法运算",
             py::arg("a"), py::arg("b"))
        .def("divide", &Calculator::divide, "除法运算",
             py::arg("a"), py::arg("b"))
        
        // 成员变量访问
        .def("set_value", &Calculator::set_value, "设置值",
             py::arg("value"))
        .def("get_value", &Calculator::get_value, "获取值")
        
        // 批量操作
        .def("sum", &Calculator::sum, "计算向量和",
             py::arg("numbers"))
        .def("average", &Calculator::average, "计算平均值",
             py::arg("numbers"))
        
        // 静态方法
        .def_static("power", &Calculator::power, "计算幂",
                    py::arg("base"), py::arg("exponent"))
        
        // 字符串方法
        .def("greet", &Calculator::greet, "问候语",
             py::arg("name"));
    
    // ========== 绑定自由函数 ==========
    m.def("compute_area", &compute_area, "计算圆的面积",
          py::arg("radius"));
    
    m.def("generate_fibonacci", &generate_fibonacci, 
          "生成斐波那契数列",
          py::arg("n"));
    
    // ========== 模块属性 ==========
    m.attr("PI") = 3.141592653589793;
    m.attr("VERSION") = "1.0.0";
}
```

### 第三步：配置构建系统

#### 3.1 CMake 配置（CMakeLists.txt）

```cmake
cmake_minimum_required(VERSION 3.12)
project(calculator)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找 Python 和 pybind11
find_package(pybind11 REQUIRED)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# 包含目录
include_directories(include)

# 源文件
set(SOURCES
    src/calculator.cpp
    python/bindings.cpp
)

# 创建 Python 模块
pybind11_add_module(calculator ${SOURCES})

# 编译选项
target_compile_options(calculator PRIVATE -O3 -Wall)

# 设置输出目录（可选）
set_target_properties(calculator PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/build"
)
```

#### 3.2 setup.py 配置（用于 pip 安装）

```python
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, Extension
import pybind11

ext_modules = [
    Pybind11Extension(
        "calculator",
        [
            "src/calculator.cpp",
            "python/bindings.cpp",
        ],
        include_dirs=["include"],
        language='c++',
        cxx_std=11,
    ),
]

setup(
    name="calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Pybind11 示例：计算器模块",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
```

---

## 高级特性

### 1. 重载函数

```cpp
// C++ 代码
double add(int a, int b);
double add(double a, double b);

// 绑定代码
.def("add", py::overload_cast<int, int>(&Calculator::add))
.def("add", py::overload_cast<double, double>(&Calculator::add))
```

### 2. 属性绑定

```cpp
// 直接访问成员变量
.def_readwrite("value", &Calculator::value_)
.def_readonly("constant", &Calculator::CONSTANT)
```

### 3. 操作符重载

```cpp
.def(py::self + py::self)  // __add__
.def(py::self - py::self)  // __sub__
.def(py::self * py::self)  // __mul__
.def(py::self / py::self)  // __truediv__
```

### 4. 回调函数

```cpp
// C++ 接受函数指针
void process_data(std::function<double(double)> func);

// Python 绑定
.def("process_data", &Calculator::process_data)
```

### 5. 异常处理

```cpp
// C++ 抛出异常
throw std::runtime_error("Error message");

// Python 自动转换为 Python 异常
```

### 6. 文档字符串

```cpp
.def("method", &Calculator::method, 
     "方法文档",                    // 简短描述
     py::arg("param") = default,   // 参数文档
     "详细描述...")                 // 详细描述
```

---

## 构建与打包

### 方法 1：使用 CMake

```bash
# 创建构建目录
mkdir build && cd build

# 配置
cmake ..

# 编译
cmake --build .

# 运行测试
python ../tests/test_calculator.py
```

### 方法 2：使用 setup.py

```bash
# 开发模式安装
pip install -e .

# 或者直接构建
python setup.py build_ext --inplace
```

### 方法 3：使用 pyproject.toml（现代方式）

创建 `pyproject.toml`：

```toml
[build-system]
requires = ["setuptools>=42", "wheel", "pybind11>=2.6.0"]
build-backend = "setuptools.build_meta"

[project]
name = "calculator"
version = "1.0.0"
requires-python = ">=3.6"
```

---

## 最佳实践

### 1. 代码组织

- ✅ 将 C++ 代码和绑定代码分离
- ✅ 使用命名空间避免冲突
- ✅ 保持头文件简洁

### 2. 性能优化

- ✅ 使用 `py::return_value_policy::reference_internal` 避免不必要的拷贝
- ✅ 对于大型数据，考虑使用 NumPy 数组
- ✅ 使用 `py::call_guard<py::gil_scoped_release>()` 释放 GIL

### 3. 错误处理

- ✅ 在 C++ 中抛出标准异常
- ✅ 提供清晰的错误消息
- ✅ 使用 `py::register_exception` 注册自定义异常

### 4. 文档

- ✅ 为所有函数和类添加文档字符串
- ✅ 使用 `py::arg` 为参数命名
- ✅ 提供使用示例

### 5. 测试

- ✅ 编写单元测试
- ✅ 测试边界情况
- ✅ 性能基准测试

---

## 常见问题

### Q1: 如何调试绑定代码？

**A:** 使用 GDB 或 LLDB：
```bash
gdb python
(gdb) run test_calculator.py
```

### Q2: 如何处理 NumPy 数组？

**A:** 使用 `pybind11/numpy.h`：
```cpp
#include <pybind11/numpy.h>
py::array_t<double> process_array(py::array_t<double> input);
```

### Q3: 如何支持多线程？

**A:** 使用 `py::call_guard<py::gil_scoped_release>()`：
```cpp
.def("thread_safe_method", &Class::method,
     py::call_guard<py::gil_scoped_release>())
```

### Q4: 如何打包为 wheel？

**A:** 使用 `python setup.py bdist_wheel` 或 `pip install build && python -m build`

### Q5: 如何处理 C++ 模板？

**A:** 使用 `py::class_<TemplateType<int>>` 或 `PYBIND11_MAKE_OPAQUE`

---

## 下一步

1. 阅读 [Pybind11 官方文档](https://pybind11.readthedocs.io/)
2. 查看示例代码
3. 尝试修改和扩展功能
4. 学习 NumPy 集成
5. 探索多线程和异步编程

---

## 参考资料

- [Pybind11 官方文档](https://pybind11.readthedocs.io/)
- [Pybind11 GitHub](https://github.com/pybind/pybind11)
- [CMake 文档](https://cmake.org/documentation/)
- [Python C API](https://docs.python.org/3/c-api/)

---

**祝您学习愉快！** 🚀

