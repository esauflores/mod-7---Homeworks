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
    # otherwise, f has a root in [c, b]
    a, b = (a, c) if f(a) * f(c) < 0 else (c, b)

    return a, b, c


def newton_step(x: float, f: callable, df: callable) -> float:
    """Performs a newton step on the function f at the point x

    Args:
        x (float): point to perform the newton step
        f (callable): function to be evaluated
        df (callable): derivative of the function f

    Returns:
        x (float): new approximation
    """

    return x - f(x) / df(x)


def combined(
    x: float,
    a: float,
    b: float,
    f: callable,
    df: callable,
    tol: float = 1e-6,
    maxsteps: float = np.Inf,
) -> (float, int, list):
    """Finds a root of the function f using the combined method

    Args:
        x (float): initial approximation
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        f (callable): function to be evaluated
        df (callable): derivative of the function f
        tol (float, optional): tolerance. Defaults to 1e-6.
        maxsteps (int): maximum number of steps to be taken


    Returns:
        x (float): approximation of the root
        steps (int): number of steps taken
        aprox (list): list of approximations
    """

    steps = 0  # number of steps taken
    aprox = [x]  # list of approximations

    while steps < maxsteps:
        steps += 1

        x1 = None
        if df(x) != 0.0:
            x1 = newton_step(x, f, df)

        if x1 is None or x1 < a or x1 > b:
            x1, a, b = bisection_step(a, b, f)
            aprox.append(x1)

            if b - a < tol:
                x = x1
                break
        else:
            a, b = (a, x1) if f(a) * f(x1) < 0 else (x1, b)
            aprox.append(x1)

            if abs(x1 - x) < tol:
                x = x1
                break
        x = x1

    return x, steps, aprox


def print_process(
    f: callable, a: float, b: float, root: float, steps: int, aprox: list, tab: int = 4
):
    """Prints the process of the combined method

    Args:
        f (callable): function to be evaluated
        a (float): left endpoint of the interval
        b (float): right endpoint of the interval
        steps (int): number of steps taken
        aprox (list): list of approximations
        tab (int, optional): number of spaces to indent. Defaults to 4.
    """
    aprox = [round(x, 6) for x in aprox]
    sp = " " * tab

    print()
    print(sp, "f(x) = {}".format(inspect.getsource(f).strip()))
    print(sp, "a = {}".format(a), ", b = {}".format(b))
    print(sp, "root = {}".format(root), ", f(root) = {}".format(f(root)))
    print(sp, "steps = {}".format(steps), "aprox = {}".format(aprox))
    print()
