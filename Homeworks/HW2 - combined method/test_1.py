# test_1.py

import combined as com


def test_1():
    #  (x-3)(x-1)^2
    f = lambda x: (x - 3) * (x - 1) ** 2
    df = lambda x: 3 * x**2 - 10 * x + 7

    x, a, b, tol, maxsteps = 2, -1000, 1000, 1e-6, 1e6

    x, a, b, steps, aprox = com.combined(x, a, b, f, df, tol, maxsteps)

    com.print_process(f, a, b, x, steps, aprox)


def test_2():
    #  (x-3)(x-1)^2
    f = lambda x: (x - 3) * (x - 1) ** 2
    df = lambda x: 3 * x**2 - 10 * x + 7

    x, a, b, tol, maxsteps = -2, -1000, 1000, 1e-6, 1e6

    x, a, b, steps, aprox = com.combined(x, a, b, f, df, tol, maxsteps)

    com.print_process(f, a, b, x, steps, aprox)


def test_3():
    #  (x-3)(x-1)^2
    f = lambda x: (x - 3) * (x - 1) ** 2
    df = lambda x: 3 * x**2 - 10 * x + 7

    x, a, b, tol, maxsteps = -1, -1000, 1000, 1e-6, 1e6

    x, a, b, steps, aprox = com.combined(x, a, b, f, df, tol, maxsteps)

    com.print_process(f, a, b, x, steps, aprox)
