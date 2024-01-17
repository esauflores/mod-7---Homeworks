# test_1.py

import numpy as np
import bisection as bis
import fixed_point as fix
import newton as new

import matplotlib.pyplot as plt

fig, axs = None, None


def test_preparation():
    global fig, axs
    # 3 subplots square
    fig, axs = plt.subplots(1, 3, figsize=(14, 14 / 3))
    print()


def test_1():
    global fig, axs

    #  (x-1)(x+1)(x-3)
    f = lambda x: (x - 1) * (x + 1) * (x - 3)
    df = lambda x: 3 * x**2 - 6 * x - 1

    xo, ao, bo, tolo, maxstepso = 0, -2, 5, 1e-6, 100
    alpha = 0.1
    i = 0

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, a, b, steps, aprox = bis.bisection(a, b, f, tol, maxsteps)
    print("bisection: ")
    bis.print_process(f, a, b, x, steps, aprox)

    # error = pn+1 - pn
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="bisection")

    g = fix.relaxation(f, alpha)
    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)
    print("fixed point: ")
    fix.print_process(f, g, x, steps, aprox)

    # plot fixed point error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="fixed point")

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = new.newton(x, f, df, tol, maxsteps)
    print("newton: ")
    new.print_process(f, x, steps, aprox)

    # plot newton error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="newton")

    axs[i].set_yscale("log")
    axs[i].set_xlabel("steps")
    axs[i].set_ylabel("error")
    axs[i].set_title("x = {} a = {} b = {} alpha = {}".format(xo, ao, bo, alpha))
    axs[i].legend()


def test_2():
    global fig, axs

    #  (x-1)(x+1)(x-3)
    f = lambda x: (x - 1) * (x + 1) * (x - 3)
    df = lambda x: 3 * x**2 - 6 * x - 1

    xo, ao, bo, tolo, maxstepso = -1.5, -2, 5, 1e-6, 100
    alpha = 1e-6
    i = 1

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, a, b, steps, aprox = bis.bisection(a, b, f, tol, maxsteps)
    print("bisection: ")
    bis.print_process(f, a, b, x, steps, aprox)

    # error = pn+1 - pn
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="bisection")

    g = fix.relaxation(f, alpha)
    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)
    print("fixed point: ")
    fix.print_process(f, g, x, steps, aprox)

    # plot fixed point error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="fixed point")

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = new.newton(x, f, df, tol, maxsteps)
    print("newton: ")
    new.print_process(f, x, steps, aprox)

    # plot newton error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="newton")

    axs[i].set_yscale("log")
    axs[i].set_xlabel("steps")
    axs[i].set_ylabel("error")
    axs[i].set_title("x = {} a = {} b = {} alpha = {}".format(xo, ao, bo, alpha))
    axs[i].legend()


def test_3():
    global fig, axs

    #  (x-1)(x+1)(x-3)
    f = lambda x: (x - 1) * (x + 1) * (x - 3)
    df = lambda x: 3 * x**2 - 6 * x - 1

    xo, ao, bo, tolo, maxstepso = 4.5, -2, 5, 1e-6, 100
    alpha = 1e-7
    i = 2

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, a, b, steps, aprox = bis.bisection(a, b, f, tol, maxsteps)
    print("bisection: ")
    bis.print_process(f, a, b, x, steps, aprox)

    # error = pn+1 - pn
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="bisection")

    g = fix.relaxation(f, alpha)
    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = fix.fixed_point(x, g, tol, maxsteps)
    print("fixed point: ")
    fix.print_process(f, g, x, steps, aprox)

    # plot fixed point error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="fixed point")

    x, a, b, tol, maxsteps = xo, ao, bo, tolo, maxstepso
    x, steps, aprox = new.newton(x, f, df, tol, maxsteps)
    print("newton: ")
    new.print_process(f, x, steps, aprox)

    # plot newton error vs steps
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    x = np.linspace(ao, bo, maxstepso)
    axs[i].plot(error, label="newton")

    axs[i].set_yscale("log")
    axs[i].set_xlabel("steps")
    axs[i].set_ylabel("error")
    axs[i].set_title("x = {} a = {} b = {} alpha = {}".format(xo, ao, bo, alpha))
    axs[i].legend()


def test_post():
    global fig, axs
    fig.tight_layout()
    plt.show()
