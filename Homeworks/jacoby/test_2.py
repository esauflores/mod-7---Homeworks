# test_1.py

import jacobi as jac
import numpy as np


def test_2():
    # big matrix

    n = 10
    l = -10
    r = 10

    blocks = np.random.randint(l, r, (n, n))
    for i in range(n):
        while blocks[i][i] == 0:
            blocks[i][i] = np.random.randint(l, r)

    res = np.random.randint(l, r, (n, 1))

    eq = []
    for i in range(n):
        eq += [[blocks[i][j] for j in range(n)] + [res[i][0]]]

    ans, steps, aprox = jac.jacobi(eq, np.Inf, 1e-6, logs=True)
    jac.print_equations(eq, ans, steps, aprox)
