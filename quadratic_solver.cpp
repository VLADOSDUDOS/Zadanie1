#include "quadratic_solver.h"
#include <cmath>

std::vector<double> solve(double a, double b, double c) {
    std::vector<double> roots;
    double discriminant = b * b - 4 * a * c;
    if (discriminant >= 0) {
        double root1 = (-b + std::sqrt(discriminant)) / (2 * a);
        double root2 = (-b - std::sqrt(discriminant)) / (2 * a);
        roots.push_back(std::min(root1, root2));
        roots.push_back(std::max(root1, root2));
    }    
    return roots;
}
