# newton.py

import numpy as np
import inspect


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


def newton(
    x: float, f: callable, df: callable, tol: float = 1e-6, maxsteps: float = np.Inf
) -> (float, int, list):
    """Finds a root of the function f using the newton method

    Args:
        x (float): initial approximation
        f (callable): function to be evaluated
        df (callable): derivative of the function f
        tol (float, optional): tolerance. Defaults to 1e-6.

    Returns:
        x (float): approximation of the root
    """

    steps = 0  # number of steps taken
    aprox = [x]  # list of approximations

    while steps < maxsteps:
        steps += 1

        x1 = newton_step(x, f, df)  # new approximation
        aprox.append(x1)

        if abs(x1 - x) < tol:
            x = x1
            break

        x = x1

    return x, steps, aprox


def print_process(f: callable, root: float, steps: int, aprox: list, tab: int = 4):
    """Prints the process of the newton method

    Args:
        f (callable): function to be evaluated
        steps (int): number of steps taken
        aprox (list): list of approximations
        tab (int, optional): number of spaces to indent. Defaults to 4.
    """

    aprox = [round(x, 6) for x in aprox]
    sp = " " * tab

    print()
    print(sp, "f(x) = {}".format(inspect.getsource(f).strip()))
    print(sp, "root = {}".format(root), "f(root) = {}".format(f(root)))
    print(sp, "steps = {}".format(steps), "aprox = {}".format(aprox))
    print()
