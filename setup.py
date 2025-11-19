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

