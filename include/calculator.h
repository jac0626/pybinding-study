#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <string>
#include <vector>

class Calculator {
public:
    Calculator();
    Calculator(double initial_value);
    
    // 基本运算
    double add(double a, double b);
    double subtract(double a, double b);
    double multiply(double a, double b);
    double divide(double a, double b);
    
    // 成员变量操作
    void set_value(double value);
    double get_value() const;
    
    // 批量操作
    double sum(const std::vector<double>& numbers);
    double average(const std::vector<double>& numbers);
    
    // 静态方法
    static double power(double base, double exponent);
    
    // 字符串操作示例
    std::string greet(const std::string& name);
    
private:
    double value_;
};

// 自由函数示例
double compute_area(double radius);
std::vector<int> generate_fibonacci(int n);

#endif // CALCULATOR_H

