# test_1.py

import jacobi as jac
import numpy as np


def test_1():
    eq = [
        [5, 1, 1, 7],
        [1, 4, -1, 4],
        [1, 2, 5, 8],
    ]

    ans, steps, aprox = jac.jacobi(eq, np.Inf, 1e-4, logs=True)

    jac.print_equations(eq, ans, steps, aprox)
