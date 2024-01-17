# test_1.py

import bisection as bis


def test_1():
    f = lambda x: x**2 - 2
    a, b, tol = 0, 7, 1e-6

    c, a, b, steps, aprox = bis.bisection(a, b, f, tol)
    bis.print_process(f, a, b, c, steps, aprox)


def test_2():
    f = lambda x: x**3 - x**2 - 1
    a, b, tol = -100, 100, 1e-6

    c, a, b, steps, aprox = bis.bisection(a, b, f, tol)
    bis.print_process(f, a, b, c, steps, aprox)
