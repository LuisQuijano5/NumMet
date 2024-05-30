import math
import numpy as np
from Model.test import gauss_jordan

# def quadratic_regression(x, y):
#
#     x = np.array(x)
#     y = np.array(y)
#
#     coeffs = np.polyfit(x, y, 2)
#     a, b, c = coeffs
#
#     equation = f"y = {a:.3f}x^2 + {b:.3f}x + {c:.3f}"
#
#     y_pred = np.polyval(coeffs, x)
#
#     ss_tot = np.sum((y - np.mean(y))**2)
#     ss_res = np.sum((y - y_pred)**2)
#     r_squared = 1 - (ss_res / ss_tot)
#
#     return equation, r_squared

def quadratic_regression(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    #calculate sums for the normal equations
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum(x**2 * y)

    augmented_matrix = np.array([
        [sum_x4, sum_x3, sum_x2, sum_x2y],
        [sum_x3, sum_x2, sum_x, sum_xy],
        [sum_x2, sum_x, n, sum_y]
    ])

    coeffs, _ = gauss_jordan(augmented_matrix)

    print(coeffs[:3])
    a, b, c = coeffs[:3]

    # Create equation string
    equation = f"y = {a:.3f}x^2 + {b:.3f}x + {c:.3f}"

    # Calculate predicted values
    y_pred = np.polyval([a, b, c], x)

    # Calculate R-squared
    ss_tot = np.sum((y - np.mean(y))**2)
    ss_res = np.sum((y - y_pred)**2)
    r_squared = 1 - (ss_res / ss_tot)

    return equation, math.sqrt(r_squared)
