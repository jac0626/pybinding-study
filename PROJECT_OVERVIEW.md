# 项目总览

## 📁 项目结构

```
py-binding/
├── README.md                 # 完整教学文档（主要文档）
├── QUICK_START.md           # 快速开始指南
├── BUILD.md                 # 详细构建指南
├── ADVANCED.md              # 高级特性教程
├── PROJECT_OVERVIEW.md      # 本文件
│
├── CMakeLists.txt           # CMake 构建配置
├── setup.py                 # setuptools 配置
├── pyproject.toml           # 现代 Python 项目配置
├── requirements.txt         # Python 依赖
├── .gitignore              # Git 忽略文件
│
├── include/                # C++ 头文件
│   └── calculator.h        # 计算器类定义
│
├── src/                    # C++ 源文件
│   └── calculator.cpp     # 计算器类实现
│
├── python/                 # Python 绑定代码
│   └── bindings.cpp        # pybind11 绑定代码
│
├── tests/                  # 测试代码
│   └── test_calculator.py # 单元测试
│
└── examples/               # 使用示例
    └── example_usage.py   # 示例代码
```

## 📚 文档说明

### 1. README.md
**主要教学文档**，包含：
- Pybind11 简介和优势
- 环境准备和安装
- 项目结构说明
- 核心概念讲解
- 详细教程（从 C++ 代码到 Python 绑定）
- 高级特性介绍
- 构建与打包方法
- 最佳实践
- 常见问题解答

### 2. QUICK_START.md
**快速开始指南**，适合：
- 想要快速上手的用户
- 已有经验的开发者
- 需要快速参考的场景

### 3. BUILD.md
**详细构建指南**，包含：
- 多种构建方法（CMake、setup.py、pyproject.toml）
- 详细的前置要求
- CMake 构建选项
- 调试构建方法
- 性能优化
- 打包分发
- 常见构建问题解决

### 4. ADVANCED.md
**高级特性教程**，涵盖：
- NumPy 集成
- 多线程与 GIL 管理
- 模板和泛型编程
- 自定义类型转换
- 异常处理
- 内存管理
- 性能优化技巧
- 调试技巧

## 🎯 学习路径

### 初学者路径
1. 阅读 `README.md` 的简介部分
2. 按照 `QUICK_START.md` 快速上手
3. 理解 `README.md` 中的详细教程
4. 运行 `tests/test_calculator.py` 和 `examples/example_usage.py`
5. 尝试修改代码并重新构建

### 进阶路径
1. 完成初学者路径
2. 阅读 `ADVANCED.md` 学习高级特性
3. 参考 `BUILD.md` 优化构建配置
4. 实现自己的 C++ 模块
5. 学习性能优化和调试技巧

## 🔧 核心文件说明

### C++ 代码
- **include/calculator.h**: 定义 `Calculator` 类和自由函数
- **src/calculator.cpp**: 实现所有 C++ 功能

### Python 绑定
- **python/bindings.cpp**: 使用 pybind11 将 C++ 代码暴露给 Python

### 构建配置
- **CMakeLists.txt**: CMake 构建系统配置
- **setup.py**: setuptools 配置，支持 `pip install`
- **pyproject.toml**: 现代 Python 项目配置

### 测试和示例
- **tests/test_calculator.py**: 完整的单元测试套件
- **examples/example_usage.py**: 详细的使用示例

## 🚀 快速命令参考

### 构建
```bash
# CMake 方式
mkdir build && cd build
cmake ..
cmake --build .

# setup.py 方式
pip install -e .

# pyproject.toml 方式
pip install build
python -m build
```

### 测试
```bash
python tests/test_calculator.py
```

### 运行示例
```bash
python examples/example_usage.py
```

## 📖 推荐阅读顺序

1. **QUICK_START.md** - 快速了解项目
2. **README.md** - 深入学习
3. **BUILD.md** - 掌握构建方法
4. **ADVANCED.md** - 探索高级特性

## 🎓 学习目标

完成本教程后，您应该能够：

- ✅ 理解 Pybind11 的基本原理
- ✅ 编写 C++ 代码并创建 Python 绑定
- ✅ 使用 CMake 或 setuptools 构建项目
- ✅ 处理基本的数据类型转换
- ✅ 绑定类、函数和静态方法
- ✅ 处理异常和错误
- ✅ 优化性能和内存使用
- ✅ 调试和测试绑定代码

## 🔗 相关资源

- [Pybind11 官方文档](https://pybind11.readthedocs.io/)
- [Pybind11 GitHub](https://github.com/pybind/pybind11)
- [CMake 文档](https://cmake.org/documentation/)
- [Python C API](https://docs.python.org/3/c-api/)

## 💡 提示

- 所有代码都包含详细的中文注释
- 测试代码展示了各种使用场景
- 示例代码可以直接运行
- 建议按照文档顺序学习

---

**祝您学习愉快！** 🎉

