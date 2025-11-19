#!/usr/bin/env python3
"""
Pybind11 计算器模块使用示例
"""

import sys
import os

# 添加构建目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))

try:
    import calculator
except ImportError:
    print("错误：无法导入 calculator 模块")
    print("请先构建模块")
    sys.exit(1)


def example_basic_usage():
    """基本使用示例"""
    print("=" * 60)
    print("示例 1：基本使用")
    print("=" * 60)
    
    # 创建计算器实例
    calc = calculator.Calculator()
    
    # 基本运算
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print()


def example_member_variables():
    """成员变量示例"""
    print("=" * 60)
    print("示例 2：成员变量操作")
    print("=" * 60)
    
    # 使用默认构造函数
    calc1 = calculator.Calculator()
    print(f"初始值: {calc1.get_value()}")
    
    # 设置值
    calc1.set_value(42.5)
    print(f"设置后的值: {calc1.get_value()}")
    
    # 使用带参数的构造函数
    calc2 = calculator.Calculator(100.0)
    print(f"构造时设置的值: {calc2.get_value()}")
    print()


def example_vector_operations():
    """向量操作示例"""
    print("=" * 60)
    print("示例 3：向量操作")
    print("=" * 60)
    
    calc = calculator.Calculator()
    
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(f"数字列表: {numbers}")
    print(f"总和: {calc.sum(numbers)}")
    print(f"平均值: {calc.average(numbers)}")
    print()


def example_static_methods():
    """静态方法示例"""
    print("=" * 60)
    print("示例 4：静态方法")
    print("=" * 60)
    
    result = calculator.Calculator.power(2, 8)
    print(f"2^8 = {result}")
    print()


def example_free_functions():
    """自由函数示例"""
    print("=" * 60)
    print("示例 5：自由函数")
    print("=" * 60)
    
    # 计算圆的面积
    radius = 10.0
    area = calculator.compute_area(radius)
    print(f"半径为 {radius} 的圆的面积: {area}")
    
    # 生成斐波那契数列
    n = 15
    fib = calculator.generate_fibonacci(n)
    print(f"前 {n} 个斐波那契数: {fib}")
    print()


def example_string_operations():
    """字符串操作示例"""
    print("=" * 60)
    print("示例 6：字符串操作")
    print("=" * 60)
    
    calc = calculator.Calculator()
    greeting = calc.greet("开发者")
    print(greeting)
    print()


def example_module_attributes():
    """模块属性示例"""
    print("=" * 60)
    print("示例 7：模块属性")
    print("=" * 60)
    
    print(f"PI = {calculator.PI}")
    print(f"版本 = {calculator.VERSION}")
    print()


def example_error_handling():
    """错误处理示例"""
    print("=" * 60)
    print("示例 8：错误处理")
    print("=" * 60)
    
    calc = calculator.Calculator()
    
    # 除零错误
    try:
        result = calc.divide(10, 0)
    except RuntimeError as e:
        print(f"捕获到除零错误: {e}")
    
    # 空向量错误
    try:
        result = calc.average([])
    except RuntimeError as e:
        print(f"捕获到空向量错误: {e}")
    print()


def main():
    """运行所有示例"""
    print("\n" + "=" * 60)
    print("Pybind11 计算器模块使用示例")
    print("=" * 60 + "\n")
    
    example_basic_usage()
    example_member_variables()
    example_vector_operations()
    example_static_methods()
    example_free_functions()
    example_string_operations()
    example_module_attributes()
    example_error_handling()
    
    print("=" * 60)
    print("所有示例运行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()

