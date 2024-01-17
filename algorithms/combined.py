import algorithms.bisection as bis
import algorithms.newton as new


def combined(x, a, b, f, df, tol = 1e-6, maxsteps = 100, process = False):
    steps, aprox, x1, x2 = 1, [x], None, None

    x1 = new.newton_step(x, f, df) if df(x) != 0 else None
    if x1 is None or x1 < a or x1 > b: a, b, x2, steps = bis.bisection_step(a, b, f) + (steps+1,)
    else: a, b, steps = ((a, x1) if f(a) * f(x1) < 0 else (x1, b)) + (steps+1,)
    
    while steps+1 < maxsteps:
        if x1 is not None and a <= x and x <= b and abs(x1-x) < tol: break
        if x2 is not None and b-a < tol: break
                         
        aprox.append(x1 if x1 is not None and a <= x1 and x1 <= b else x2)
        x = x1 if x1 is not None and a <= x1 and x1 <= b else x2
        
        x1 = new.newton_step(x, f, df) if df(x) != 0 else None
        if x1 is None or x1 < a or x1 > b: a, b, x2, steps = bis.bisection_step(a, b, f) + (steps+1,)
        else: a, b, steps = ((a, x1) if f(a) * f(x1) <= 0 else (x1, b)) + (steps+1,)
    
    aprox.append(x1 if x1 is not None and a <= x1 and x1 <= b else x2); steps += 1
    
    if process: print_process(a, b, x, f, tol, steps, aprox)
    
    return a, b, x, steps, aprox


def print_process(a, b, root, f, tol, steps, aprox):
    print()
    print(f"a = {a}, b = {b}")
    print(f"root = {root}, f(root) = {f(root)}")
    if(len(aprox) <= 100): print(f"steps = {steps}, aprox = {[round(x, 2) for x in aprox]}")
    else: print(f"steps = {steps}, aprox too long to print")
    print(f"Tol error =", abs(f(root)) < tol)
    print()
