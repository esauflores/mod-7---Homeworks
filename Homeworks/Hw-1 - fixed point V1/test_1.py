# test_1.py

import fixed_point as fix


def test_1():
    f = lambda x: x**2 - 4
    g = fix.relaxation(f, 0.5)
    x, tol, maxsteps = 1.5, 1e-6, 100

    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)

    fix.print_process(f, g, x, steps, aprox)


def test_2():
    f = lambda x: x**2 - 4
    g = fix.relaxation(f, 0.1)

    x, tol, maxsteps = 1.2, 1e-6, 1e6

    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)

    fix.print_process(f, g, x, steps, aprox)


def test_3():
    f = lambda x: x**2 - 4
    g = fix.relaxation(f, 0.000001)

    x, tol, maxsteps = 0.5, 1e-6, 1e6

    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)

    fix.print_process(f, g, x, steps, [])
