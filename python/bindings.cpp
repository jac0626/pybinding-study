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

