#include "calculator.h"
#include <numeric>
#include <cmath>
#include <algorithm>
#include <stdexcept>

Calculator::Calculator() : value_(0.0) {}

Calculator::Calculator(double initial_value) : value_(initial_value) {}

double Calculator::add(double a, double b) {
    return a + b;
}

double Calculator::subtract(double a, double b) {
    return a - b;
}

double Calculator::multiply(double a, double b) {
    return a * b;
}

double Calculator::divide(double a, double b) {
    if (b == 0.0) {
        throw std::runtime_error("Division by zero!");
    }
    return a / b;
}

void Calculator::set_value(double value) {
    value_ = value;
}

double Calculator::get_value() const {
    return value_;
}

double Calculator::sum(const std::vector<double>& numbers) {
    return std::accumulate(numbers.begin(), numbers.end(), 0.0);
}

double Calculator::average(const std::vector<double>& numbers) {
    if (numbers.empty()) {
        throw std::runtime_error("Cannot compute average of empty vector");
    }
    return sum(numbers) / numbers.size();
}

double Calculator::power(double base, double exponent) {
    return std::pow(base, exponent);
}

std::string Calculator::greet(const std::string& name) {
    return "Hello, " + name + "! Welcome to Pybind11!";
}

// 自由函数实现
double compute_area(double radius) {
    return 3.141592653589793 * radius * radius;
}

std::vector<int> generate_fibonacci(int n) {
    if (n <= 0) return {};
    if (n == 1) return {0};
    if (n == 2) return {0, 1};
    
    std::vector<int> fib = {0, 1};
    for (int i = 2; i < n; ++i) {
        fib.push_back(fib[i-1] + fib[i-2]);
    }
    return fib;
}

