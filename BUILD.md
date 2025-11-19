# 构建指南

## 快速开始

### 方法 1：使用 CMake（推荐）

```bash
# 1. 安装依赖
pip install pybind11

# 2. 创建构建目录
mkdir build && cd build

# 3. 配置项目
cmake ..

# 4. 编译
cmake --build .

# 5. 运行测试
python ../tests/test_calculator.py

# 6. 运行示例
python ../examples/example_usage.py
```

### 方法 2：使用 setup.py

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 开发模式安装
pip install -e .

# 或者直接构建
python setup.py build_ext --inplace
```

### 方法 3：使用 pyproject.toml（现代方式）

```bash
# 1. 安装构建工具
pip install build

# 2. 构建 wheel
python -m build

# 3. 安装
pip install dist/calculator-1.0.0-*.whl
```

## 详细步骤

### 前置要求

1. **安装 C++ 编译器**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install build-essential
   
   # macOS
   xcode-select --install
   
   # Windows
   # 安装 Visual Studio 或 MinGW
   ```

2. **安装 CMake**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install cmake
   
   # macOS
   brew install cmake
   
   # 或使用 pip
   pip install cmake
   ```

3. **安装 Python 开发头文件**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3-dev
   
   # macOS (通常已包含)
   # Windows (通常已包含)
   ```

### CMake 构建选项

```bash
# 指定 Python 版本
cmake -DPYTHON_VERSION=3.9 ..

# 指定构建类型
cmake -DCMAKE_BUILD_TYPE=Release ..

# 指定安装路径
cmake -DCMAKE_INSTALL_PREFIX=/usr/local ..
```

### 调试构建

```bash
# Debug 模式
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build .

# 使用 GDB 调试
gdb python
(gdb) run ../tests/test_calculator.py
```

## 常见问题

### 问题 1：CMake 错误 "Could not find CMAKE_ROOT"

**症状：**
```
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
```

**原因：** 虚拟环境中通过 pip 安装的 cmake 包不完整，只有 Python 包装器，没有实际的 CMake 可执行文件。

**解决方案：**
```bash
# 1. 删除虚拟环境中的损坏的 cmake 符号链接
rm -f .venv/bin/cmake .venv/bin/ccmake .venv/bin/cmake-gui

# 2. 使用系统级的 CMake（推荐）
# 确保系统已安装 CMake
# Ubuntu/Debian:
sudo apt-get install cmake

# macOS:
brew install cmake

# 3. 验证 CMake 可用
which cmake
cmake --version
```

### 问题 2：找不到 pybind11

**症状：**
```
Could not find a package configuration file provided by "pybind11"
```

**解决方案：**
```bash
# 安装 pybind11
pip install pybind11

# 验证安装
python3 -c "import pybind11; print(pybind11.get_cmake_dir())"
```

**注意：** 本项目的 CMakeLists.txt 已自动处理通过 pip 安装的 pybind11 的查找。

### 问题 3：找不到 Python.h

**解决方案：**
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev

# 或指定 Python 路径
cmake -DPYTHON_INCLUDE_DIR=/usr/include/python3.9 ..
```

### 问题 4：编译错误 "runtime_error is not a member of std"

**症状：**
```
error: 'runtime_error' is not a member of 'std'
```

**解决方案：**
在 C++ 源文件中添加头文件：
```cpp
#include <stdexcept>
```

### 问题 5：链接错误

**解决方案：**
确保安装了 Python 开发库，并检查 CMakeLists.txt 中的链接设置。

### 问题 6：模块导入失败

**解决方案：**
- 检查模块文件是否在正确的位置（通常在 `build/` 目录）
- 检查 Python 路径设置
- 确保模块名称与文件名匹配
- 尝试：`python3 -c "import sys; sys.path.insert(0, 'build'); import calculator"`

## 性能优化

### 发布构建

```bash
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --config Release
```

### 启用优化选项

在 CMakeLists.txt 中添加：
```cmake
target_compile_options(calculator PRIVATE -O3 -march=native)
```

## 打包分发

### 创建 wheel

```bash
python setup.py bdist_wheel
```

### 创建源码包

```bash
python setup.py sdist
```

### 上传到 PyPI

```bash
pip install twine
twine upload dist/*
```

