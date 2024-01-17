# bisection.py

import numpy as np
import inspect


def bisection_step(a: float, b: float, f: callable) -> (float, float, float):
    """Performs a bisection step on the interval [a, b] of the function f

    Args:
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        f (callable): function to be evaluated

    Returns:
        a (float): left endpoint of the new interval
        b (float): right endpoint of the new interval
        c (float): midpoint of the new interval
    """

    c = (a + b) / 2  # midpoint of the interval
    # if f(a) and f(c) have opposite signs, by  continuity, f has a root in [a, c]
    a, b = (a, c) if f(a) * f(c) < 0 else (c, b)

    return a, b, c


def bisection(
    a: float, b: float, f: callable, tol: float = 1e-6, maxsteps: float = np.Inf
) -> (float, float, float, int, list):
    """Finds a root of the function f in the interval [a, b] using the bisection method

    Args:
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        f (callable): function to be evaluated
        tol (float, optional): tolerance. Defaults to 1e-6
        maxsteps (int): maximum number of steps to be taken

    Returns:
        c (float): approximation of the root
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        steps (int): number of steps taken
        aprox (list): list of approximations
    """

    steps = 0  # number of steps taken
    aprox = []  # list of approximations

    # if f(a) and f(b) have the same sign, by the intermediate value theorem, f has no root in [a, b]
    if f(a) * f(b) > 0:
        return 0, 0, 0, 0, []

    # while the length of the interval is greater than the tolerance, perform a bisection step o
    # if the maximum number of steps is reached, stop
    while steps < maxsteps:
        steps += 1

        a, b, c = bisection_step(a, b, f)
        aprox.append(c)

        if b - a <= tol:
            break

    return c, a, b, steps, aprox


def print_process(
    f: callable, a: float, b: float, c: float, steps: int, aprox: list, tab: int = 4
):
    """Prints the process of the bisection method

    Args:
        f (callable): function to be evaluated
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        c (float): approximation of the root
        steps (int): number of steps taken
        aprox (list): list of approximations
        tab (int, optional): number of spaces to indent. Defaults to 4.
    """
    aprox = [round(x, 6) for x in aprox]
    sp = " " * tab

    print()
    print(sp, "f(x) = {}".format(inspect.getsource(f).strip()))
    print(sp, "a = {}".format(a), ", b = {}".format(b))
    print(sp, "root = {}".format(c), ", f(root) = {}".format(f(c)))
    print(sp, "steps = {}".format(steps), "aprox = {}".format(aprox))
    print()
