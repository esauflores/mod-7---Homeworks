def newton_step(x, f, df):
    return x - f(x) / df(x)


def newton(x, f, df, tol = 1e-6, maxsteps = 100, process = False):
    steps, aprox = 1, [x]

    x1 = newton_step(x, f, df)
    while abs(x1 - x) >= tol and steps+1 < maxsteps:
        aprox.append(x1)        
        x, x1, steps = x1, newton_step(x1, f, df), steps + 1

    aprox.append(x1); steps += 1
    
    if process: print_process(x, f, tol, steps, aprox)
    
    return x, steps, aprox


def print_process(root, f, tol, steps, aprox):
    print()
    print(f"root = {root}, f(root) = {f(root)}")
    if(len(aprox) <= 100): print(f"steps = {steps}, aprox = {[round(x, 2) for x in aprox]}")
    else: print(f"steps = {steps}, aprox too long to print")
    print(f"Tol error =", abs(f(root)) < tol)
    print()
    
    
def plot(axs, aprox):
    error = [abs(aprox[i + 1] - aprox[i]) for i in range(len(aprox) - 1)]
    axs.plot(error, label="newton")
  
