cmake_minimum_required(VERSION 3.12)
project(calculator)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找 Python
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# 查找 pybind11（通过 Python 包查找 CMake 配置）
execute_process(
    COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
)

# 设置 pybind11 的 CMake 路径
if(pybind11_DIR)
    list(APPEND CMAKE_PREFIX_PATH "${pybind11_DIR}")
endif()

# 查找 pybind11 包
find_package(pybind11 REQUIRED)

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

