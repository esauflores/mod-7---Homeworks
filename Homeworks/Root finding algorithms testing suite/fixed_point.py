# relaxation.py

import numpy as np
import inspect


def relaxation(f: callable, alpha: float) -> callable:
    """Performs a relaxation step on the function f with parameter alpha

    Args:
        f (callable): function to be evaluated
        alpha (float): relaxation parameter

    Returns:
        g (callable): function to be evaluated
    """
    g = lambda x: alpha * f(x) + x
    return g


def fixed_point_step(x: float, f: callable) -> float:
    """Performs a fixed point step on the function f at the point x

    Args:
        x (float): point to perform the fixed point step
        f (callable): function to be evaluated

    Returns:
        x (float): new approximation
    """

    return f(x)


def fixed_point(
    x: float, f: callable, tol: float = 1e-6, maxsteps: float = np.Inf
) -> float:
    """Finds a root of the function f using the fixed point method

    Args:
        x (float): initial approximation
        f (callable): function to be evaluated
        tol (float, optional): tolerance. Defaults to 1e-6.

    Returns:

    """

    steps = 0  # number of steps taken
    aprox = [x]  # list of approximations

    while steps < maxsteps:
        steps += 1

        x1 = fixed_point_step(x, f)
        aprox.append(x1)

        if abs(x1 - x) < tol:
            x = x1
            break

        x = x1

    return x, steps, aprox


def print_process(
    f: callable, g: callable, root: float, steps: int, aprox: list, tab: int = 4
):
    """Prints the process of the fixed point method

    Args:
        f (callable): function to be evaluated
        g (callable): function to be evaluated
        root (float): root of the function f
        steps (int): number of steps taken
        aprox (list): list of approximations
        tab (int, optional): number of spaces to indent. Defaults to 4.
    """
    aprox = [round(x, 6) for x in aprox]
    sp = " " * tab

    print()
    print(sp, "f(x) = {}".format(inspect.getsource(f).strip()))
    print(sp, "g(x) = {}".format(inspect.getsource(g).strip()))
    print(sp, "root = {}".format(root), "f(root) = {}".format(f(root)))
    print(sp, "steps = {}".format(steps), "aprox = {}".format(aprox))
    print()
