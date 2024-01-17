def relaxation(f, alpha):
    return lambda x: alpha * f(x) + x


def fixed_point_step(x, f):
    return f(x)


def fixed_point(x, f, alpha, tol = 1e-6, maxsteps = 100, process = False):
    steps, aprox, g = 1, [x], relaxation(f, alpha)
    
    x1 = fixed_point_step(x, f)
    while abs(x1-x) >= tol and steps+1 < maxsteps:
        aprox.append(x1)
        x, x1, steps = x1, fixed_point_step(x1, g), steps+1      
      
    aprox.append(x1); steps += 1

    if process: print_process(x, f, alpha, g, tol, steps, aprox)

    return x, steps, aprox


def print_process(root, f, alpha, g, tol, steps, aprox):
    print()
    print(f"root = {root}, f(root) = {f(root)}")
    print(f"alpha = {alpha}, g(x) = {g(root)}")
    if(len(aprox) <= 100): print(f"steps = {steps}, aprox = {[round(x, 2) for x in aprox]}")
    else: print(f"steps = {steps}, aprox too long to print")
    print(f"Tol error in g and root =", abs(g(root) - root) < tol)
    print()
  
def plot(axs, aprox):
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    axs.plot(error, label="fixed point")