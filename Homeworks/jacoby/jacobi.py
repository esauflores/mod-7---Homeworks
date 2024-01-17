# jacoby.py

import numpy as np


# Jacobi method
def euclidean_distance(x0: list, x1: list) -> float:
    res = 0
    for i in range(len(x0)):
        res += (x0[i] - x1[i]) ** 2
    return res**0.5


def jacobi_step(x0: list, equations: list) -> list:
    x1 = x0.copy()
    n = len(equations)

    for i in range(n):
        res = 0
        for j in range(n):
            res += equations[i][j] * x0[j]
        res -= equations[i][i] * x0[i]
        x1[i] = (equations[i][-1] - res) / equations[i][i]

    return x1


def jacobi(equations, maxsteps=np.Inf, tol=1e-6, logs=False):
    eq = equations.copy()
    n = len(eq)

    x0 = [i + 1 for i in range(n)]
    steps = 0
    aprox = [x0]

    # return x0, steps, aprox

    if logs:
        print(x0)

    while steps < maxsteps:
        steps += 1
        x1 = jacobi_step(x0, eq)
        aprox.append(x1)

        if logs:
            print(x1)

        if euclidean_distance(x0, x1) < tol:
            return x1, steps, aprox

        x0 = x1

    return x0, steps, aprox


def check_ans(equations, ans, tol=1e-6):
    n = len(equations)
    for i in range(n):
        res = 0
        for j in range(n):
            res += equations[i][j] * ans[j]

        if abs(res - equations[i][-1]) > tol:
            return False
    return True


def print_equations(equations, ans, steps, aprox):
    print()

    n = len(equations)

    for eq in equations:
        eqstr = ""
        for i in range(n):
            eqstr += str(eq[i]) + "x" + str(i + 1) + (" + " if i != n - 1 else " = ")
        eqstr += str(eq[-1])
        print(eqstr)

    print()

    for ap in aprox:
        print(ap)
    print()

    ans = [round(i, 6) for i in ans]

    print("steps:", steps)
    print("Answer: ", ans)
    print("Ok =", check_ans(equations, ans, tol=1e-6))
