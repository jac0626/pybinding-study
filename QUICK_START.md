# 快速开始指南

## 5 分钟快速上手

### 步骤 1：安装依赖

```bash
pip install pybind11 cmake
```

### 步骤 2：构建项目

```bash
mkdir build && cd build
cmake ..
cmake --build .
```

### 步骤 3：测试

```bash
python ../tests/test_calculator.py
```

### 步骤 4：运行示例

```bash
python ../examples/example_usage.py
```

## 最简单的示例

### C++ 代码（simple.cpp）

```cpp
#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(simple, m) {
    m.def("add", &add, "两个数相加");
}
```

### 编译

```bash
c++ -O3 -Wall -shared -std=c++11 -fPIC \
    `python3 -m pybind11 --includes` \
    simple.cpp -o simple`python3-config --extension-suffix`
```

### 使用

```python
import simple
print(simple.add(2, 3))  # 输出: 5
```

## 常见问题快速解决

### 问题：找不到 pybind11

```bash
pip install pybind11
```

### 问题：找不到 Python.h

```bash
# Ubuntu/Debian
sudo apt-get install python3-dev
```

### 问题：编译错误

检查 C++ 编译器版本：
```bash
g++ --version  # 需要 >= 4.8
```

## 下一步

- 阅读 [README.md](README.md) 了解完整教程
- 查看 [ADVANCED.md](ADVANCED.md) 学习高级特性
- 参考 [BUILD.md](BUILD.md) 了解详细构建选项

