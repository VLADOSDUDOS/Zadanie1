#include "quadratic_solver.h"
#include <iostream>
#include <Windows.h>

int main() {
    double a, b, c;
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    std::cout << "Введите коэффициенты a, b, c: ";
    std::cin >> a >> b >> c;
    std::vector<double> roots = solve(a, b, c);
    std::cout << "Корни уравнения: ";
    for (double root : roots) {
        std::cout << root << " ";
    }
    std::cout << std::endl;

    return 0;
}
