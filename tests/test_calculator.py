#!/usr/bin/env python3
"""
Pybind11 计算器模块测试
"""

import sys
import os

# 添加构建目录到路径（用于开发测试）
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))

try:
    import calculator
except ImportError:
    print("错误：无法导入 calculator 模块")
    print("请先构建模块：")
    print("  mkdir build && cd build")
    print("  cmake .. && cmake --build .")
    sys.exit(1)


def test_basic_operations():
    """测试基本运算"""
    print("=" * 50)
    print("测试基本运算")
    print("=" * 50)
    
    calc = calculator.Calculator()
    
    # 加法
    assert calc.add(2, 3) == 5, "加法测试失败"
    print("✓ 加法测试通过")
    
    # 减法
    assert calc.subtract(5, 3) == 2, "减法测试失败"
    print("✓ 减法测试通过")
    
    # 乘法
    assert calc.multiply(3, 4) == 12, "乘法测试失败"
    print("✓ 乘法测试通过")
    
    # 除法
    assert calc.divide(10, 2) == 5, "除法测试失败"
    print("✓ 除法测试通过")
    
    # 除零异常
    try:
        calc.divide(10, 0)
        assert False, "应该抛出除零异常"
    except RuntimeError as e:
        assert "zero" in str(e).lower(), "异常消息不正确"
        print("✓ 除零异常测试通过")


def test_member_variables():
    """测试成员变量"""
    print("\n" + "=" * 50)
    print("测试成员变量")
    print("=" * 50)
    
    calc = calculator.Calculator()
    assert calc.get_value() == 0.0, "初始值应为 0"
    print("✓ 初始值测试通过")
    
    calc.set_value(42.5)
    assert calc.get_value() == 42.5, "设置值失败"
    print("✓ 设置值测试通过")
    
    calc2 = calculator.Calculator(100.0)
    assert calc2.get_value() == 100.0, "构造函数初始值失败"
    print("✓ 构造函数初始值测试通过")


def test_vector_operations():
    """测试向量操作"""
    print("\n" + "=" * 50)
    print("测试向量操作")
    print("=" * 50)
    
    calc = calculator.Calculator()
    
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert calc.sum(numbers) == 15.0, "求和失败"
    print("✓ 求和测试通过")
    
    assert calc.average(numbers) == 3.0, "平均值计算失败"
    print("✓ 平均值测试通过")
    
    # 空向量异常
    try:
        calc.average([])
        assert False, "应该抛出空向量异常"
    except RuntimeError:
        print("✓ 空向量异常测试通过")


def test_static_methods():
    """测试静态方法"""
    print("\n" + "=" * 50)
    print("测试静态方法")
    print("=" * 50)
    
    result = calculator.Calculator.power(2, 3)
    assert result == 8.0, "幂运算失败"
    print("✓ 静态方法测试通过")


def test_free_functions():
    """测试自由函数"""
    print("\n" + "=" * 50)
    print("测试自由函数")
    print("=" * 50)
    
    # 计算面积
    area = calculator.compute_area(5.0)
    expected = 3.141592653589793 * 25.0
    assert abs(area - expected) < 1e-10, "面积计算失败"
    print("✓ 面积计算测试通过")
    
    # 斐波那契数列
    fib = calculator.generate_fibonacci(10)
    expected_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib == expected_fib, "斐波那契数列生成失败"
    print("✓ 斐波那契数列测试通过")


def test_string_operations():
    """测试字符串操作"""
    print("\n" + "=" * 50)
    print("测试字符串操作")
    print("=" * 50)
    
    calc = calculator.Calculator()
    greeting = calc.greet("Python")
    assert "Hello" in greeting and "Python" in greeting, "问候语失败"
    print("✓ 字符串操作测试通过")


def test_module_attributes():
    """测试模块属性"""
    print("\n" + "=" * 50)
    print("测试模块属性")
    print("=" * 50)
    
    assert hasattr(calculator, 'PI'), "模块缺少 PI 属性"
    assert calculator.PI == 3.141592653589793, "PI 值不正确"
    print("✓ PI 属性测试通过")
    
    assert hasattr(calculator, 'VERSION'), "模块缺少 VERSION 属性"
    assert calculator.VERSION == "1.0.0", "VERSION 值不正确"
    print("✓ VERSION 属性测试通过")


def main():
    """运行所有测试"""
    print("\n" + "=" * 50)
    print("开始运行 Pybind11 计算器模块测试")
    print("=" * 50 + "\n")
    
    try:
        test_basic_operations()
        test_member_variables()
        test_vector_operations()
        test_static_methods()
        test_free_functions()
        test_string_operations()
        test_module_attributes()
        
        print("\n" + "=" * 50)
        print("✓ 所有测试通过！")
        print("=" * 50)
        return 0
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

