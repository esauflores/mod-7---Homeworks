def bisection_step(a, b, f):
    c = (a + b) / 2
    a, b = (a, c) if f(a) * f(c) <= 0 else (c, b)
    return a, b, c


def bisection(a, b, f, tol, maxsteps = 100, process = False):
    steps, aprox = 0, []
    
    while b - a >= tol and steps+1 < maxsteps:
        a, b, c, steps = bisection_step(a, b, f) + (steps + 1,)
        aprox.append(c)

    a, b, c, steps = bisection_step(a, b, f) + (steps + 1,)
    aprox.append(c)
    
    if process: print_process(a, b, c, f, tol, steps, aprox)
    
    return a, b, c, steps, aprox


def print_process(a, b, root, f, tol, steps, aprox):
    print()
    print(f"a = {a}, b = {b}")
    print(f"root = {root}, f(root) = {f(root)}")
    if(len(aprox) <= 100): print(f"steps = {steps}, aprox = {[round(x, 2) for x in aprox]}")
    else: print(f"steps = {steps}, aprox too long to print")
    print(f"Tol error =", abs(f(root)) < tol)
    print()

def plot(axs, aprox):
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    axs.plot(error, label="bisection")