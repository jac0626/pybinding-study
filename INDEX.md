# Pybind11 教学项目索引

## 📑 文档导航

### 入门文档
- **[QUICK_START.md](QUICK_START.md)** - 5 分钟快速上手
- **[README.md](README.md)** - 完整教学文档（推荐从这里开始）

### 进阶文档
- **[BUILD.md](BUILD.md)** - 详细构建指南
- **[ADVANCED.md](ADVANCED.md)** - 高级特性教程

### 参考文档
- **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - 项目总览和结构说明
- **[INDEX.md](INDEX.md)** - 本文件（文档索引）

## 📂 代码文件

### C++ 源代码
- `include/calculator.h` - 计算器类头文件
- `src/calculator.cpp` - 计算器类实现

### Python 绑定
- `python/bindings.cpp` - pybind11 绑定代码

### 构建配置
- `CMakeLists.txt` - CMake 构建配置
- `setup.py` - setuptools 配置
- `pyproject.toml` - 现代 Python 项目配置
- `requirements.txt` - Python 依赖

### 测试和示例
- `tests/test_calculator.py` - 单元测试
- `examples/example_usage.py` - 使用示例

## 🎯 快速导航

### 我想...

#### 快速开始
→ 阅读 [QUICK_START.md](QUICK_START.md)

#### 系统学习
→ 阅读 [README.md](README.md)

#### 了解如何构建
→ 阅读 [BUILD.md](BUILD.md)

#### 学习高级特性
→ 阅读 [ADVANCED.md](ADVANCED.md)

#### 了解项目结构
→ 阅读 [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

#### 运行测试
→ 执行 `python tests/test_calculator.py`

#### 查看示例
→ 执行 `python examples/example_usage.py`

## 📚 学习路径

```
开始
  ↓
QUICK_START.md (快速了解)
  ↓
README.md (系统学习)
  ↓
运行 tests/ 和 examples/
  ↓
BUILD.md (掌握构建)
  ↓
ADVANCED.md (高级特性)
  ↓
实践和扩展
```

## 🔍 主题索引

### 基础主题
- [环境准备](README.md#环境准备)
- [项目结构](README.md#项目结构)
- [核心概念](README.md#核心概念)
- [详细教程](README.md#详细教程)

### 构建相关
- [CMake 构建](BUILD.md#方法-1使用-cmake推荐)
- [setup.py 构建](BUILD.md#方法-2使用-setuppy)
- [打包分发](BUILD.md#打包分发)

### 高级主题
- [NumPy 集成](ADVANCED.md#numpy-集成)
- [多线程](ADVANCED.md#多线程与-gil)
- [模板编程](ADVANCED.md#模板和泛型编程)
- [性能优化](ADVANCED.md#性能优化技巧)

## 💡 常用命令

```bash
# 安装依赖
pip install -r requirements.txt

# CMake 构建
mkdir build && cd build
cmake .. && cmake --build .

# 运行测试
python tests/test_calculator.py

# 运行示例
python examples/example_usage.py
```

## 📖 推荐阅读

1. **首次使用** → [QUICK_START.md](QUICK_START.md)
2. **深入学习** → [README.md](README.md)
3. **遇到构建问题** → [BUILD.md](BUILD.md)
4. **需要高级功能** → [ADVANCED.md](ADVANCED.md)

---

**开始您的 Pybind11 学习之旅！** 🚀

