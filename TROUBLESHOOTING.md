# 故障排除指南

## 🔧 常见问题快速解决

### CMake 相关问题

#### 问题：CMake 找不到 CMAKE_ROOT

**错误信息：**
```
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found in
/path/to/.venv/share/cmake-3.26
```

**原因：**
虚拟环境中通过 `pip install cmake` 安装的 cmake 包不完整，只包含 Python 包装器，没有实际的 CMake 可执行文件和模块。

**解决方法：**

1. **删除虚拟环境中的损坏符号链接：**
```bash
rm -f .venv/bin/cmake .venv/bin/ccmake .venv/bin/cmake-gui .venv/bin/cpack .venv/bin/ctest
```

2. **安装系统级 CMake：**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install cmake

# macOS
brew install cmake

# 或使用包管理器安装
```

3. **验证安装：**
```bash
which cmake
cmake --version
```

4. **重新运行 CMake：**
```bash
cd build
cmake ..
```

---

### Pybind11 相关问题

#### 问题：找不到 pybind11 CMake 配置

**错误信息：**
```
Could not find a package configuration file provided by "pybind11"
```

**解决方法：**

1. **安装 pybind11：**
```bash
pip install pybind11
```

2. **验证安装：**
```bash
python3 -c "import pybind11; print(pybind11.get_cmake_dir())"
```

3. **如果仍然失败，手动指定路径：**
```bash
# 获取 pybind11 路径
PYBIND11_DIR=$(python3 -c "import pybind11; print(pybind11.get_cmake_dir())")

# 使用该路径配置 CMake
cmake -Dpybind11_DIR="$PYBIND11_DIR" ..
```

**注意：** 本项目的 CMakeLists.txt 已自动处理此问题。

---

### 编译错误

#### 问题：缺少头文件

**错误信息：**
```
error: 'runtime_error' is not a member of 'std'
error: 'vector' is not a member of 'std'
```

**解决方法：**
在 C++ 源文件中添加相应的头文件：

```cpp
#include <stdexcept>  // 用于 std::runtime_error
#include <vector>     // 用于 std::vector
#include <string>     // 用于 std::string
```

#### 问题：链接错误

**错误信息：**
```
undefined reference to ...
```

**解决方法：**

1. **检查是否安装了 Python 开发库：**
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev

# 检查头文件是否存在
ls /usr/include/python3.*/Python.h
```

2. **检查 CMakeLists.txt 中的链接设置**

3. **清理并重新构建：**
```bash
rm -rf build
mkdir build && cd build
cmake ..
cmake --build .
```

---

### Python 导入问题

#### 问题：无法导入模块

**错误信息：**
```
ModuleNotFoundError: No module named 'calculator'
ImportError: dynamic module does not define module export function
```

**解决方法：**

1. **检查模块文件是否存在：**
```bash
ls -la build/calculator*.so
# 或
ls -la build/calculator*.pyd  # Windows
```

2. **检查 Python 路径：**
```python
import sys
sys.path.insert(0, 'build')  # 添加构建目录到路径
import calculator
```

3. **检查模块名称匹配：**
- CMakeLists.txt 中的模块名：`calculator`
- Python 导入：`import calculator`
- 文件名：`calculator.cpython-*.so`

4. **检查 Python 版本兼容性：**
```bash
python3 --version
# 确保编译时使用的 Python 版本与运行时一致
```

---

### 运行时错误

#### 问题：段错误（Segmentation Fault）

**可能原因：**
- 内存访问错误
- 未初始化的指针
- 类型不匹配

**调试方法：**

1. **使用 GDB：**
```bash
gdb python3
(gdb) run tests/test_calculator.py
(gdb) backtrace
```

2. **使用 Valgrind（Linux）：**
```bash
valgrind --leak-check=full python3 tests/test_calculator.py
```

3. **检查代码中的内存管理**

#### 问题：异常未正确转换

**解决方法：**
确保 C++ 代码抛出标准异常：
```cpp
#include <stdexcept>
throw std::runtime_error("错误消息");
```

---

### 性能问题

#### 问题：性能不如预期

**优化建议：**

1. **使用 Release 模式编译：**
```bash
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

2. **启用优化选项：**
在 CMakeLists.txt 中：
```cmake
target_compile_options(calculator PRIVATE -O3 -march=native)
```

3. **释放 GIL（对于长时间运行的操作）：**
```cpp
.def("long_running", &Class::method,
     py::call_guard<py::gil_scoped_release>())
```

---

## 🔍 调试技巧

### 1. 启用详细输出

```bash
# CMake 详细输出
cmake --build . --verbose

# 编译详细输出
cmake -DCMAKE_VERBOSE_MAKEFILE=ON ..
```

### 2. 检查编译命令

```bash
# 查看实际使用的编译命令
cmake --build . --verbose 2>&1 | grep "g++\|clang"
```

### 3. Python 调试

```python
import sys
print(sys.path)
print(sys.version)

# 检查模块信息
import calculator
print(calculator.__file__)
print(dir(calculator))
```

### 4. 使用 pdb 调试

```python
import pdb
pdb.set_trace()
result = calculator.add(2, 3)
```

---

## 📋 检查清单

遇到问题时，按以下顺序检查：

- [ ] CMake 是否正确安装并可用
- [ ] pybind11 是否已安装
- [ ] Python 开发库是否已安装
- [ ] C++ 编译器是否可用
- [ ] 所有必要的头文件是否包含
- [ ] 模块文件是否成功生成
- [ ] Python 路径是否正确
- [ ] Python 版本是否匹配

---

## 🆘 获取帮助

如果以上方法都无法解决问题：

1. **检查日志：** 查看完整的错误输出
2. **清理重建：** `rm -rf build && mkdir build && cd build && cmake ..`
3. **查看文档：** 参考 [README.md](README.md) 和 [BUILD.md](BUILD.md)
4. **搜索问题：** 在 [Pybind11 GitHub Issues](https://github.com/pybind/pybind11/issues) 中搜索类似问题
5. **提供信息：** 如果寻求帮助，请提供：
   - 操作系统和版本
   - Python 版本
   - CMake 版本
   - 完整的错误信息
   - 相关配置文件内容

---

**祝您顺利解决问题！** 🚀

