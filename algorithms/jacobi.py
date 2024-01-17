import numpy as np

def jacobi_step(x0: list, equations: list) -> list:
    n, x1 = len(x0), [0 for _ in range(len(x0))]
    
    for i in range(n):
        res = 0
        for j in range(n):
            if i != j: res += equations[i][j] * x0[j]
        x1[i] = (equations[i][-1] - res) / equations[i][i]
        
    return x1


def jacobi(equations, tol = 1e-6, maxsteps = 100, process = False):
    x0 = [i+1 for i in range(len(equations))]  
    eq, steps, aprox = equations, 1, [x0]
    
    if process: print_equations(equations)

    x1 = jacobi_step(x0, eq)
    while distance(x0, x1) >= tol and steps+1 < maxsteps:
        x0 = x1; steps += 1; aprox.append(x1)
        x1 = jacobi_step(x0, eq)
        
    x0 = x1; aprox.append(x1); steps += 1
    
    if process: print_process(aprox, equations, tol)
    
    return x0

def distance(x0, x1):
    dist, n = 0, len(x0)

    for i in range(n): dist += (x1[i] - x0[i]) ** 2
        
    return dist ** 0.5
    
def diagonal_dominant_matrix(n):
    equations = np.random.randint(-10, 10, size=(n, n+1))
    
    for i in range(n):
        for j in range(n):
            if i != j: equations[i][i] += abs(equations[i][j])
        equations[i][i] += np.random.randint(1, 10)
        
    
    for i in range(n):
        equations[i][-1] = 0
        for j in range(n): equations[i][-1] += equations[i][j]
        
        
    return equations

def print_equations(equations):
    print()
    n = len(equations)
    for i in range(n):
        for j in range(n):
            print(f'{equations[i][j]}x{j}', end=' ')
            if j < n - 1: print('+', end=' ')
        print('=', equations[i][-1])
    print()

def print_process(aprox, equations, tol):
    print()
    if len(aprox) <= 100: 
        for i in range(len(aprox)): print(f'x{i} = {aprox[i]}')
    else: print('Aprox too long to print')
    
    print()
    for eq in equations:
        res = 0
        for i in range(len(aprox[-1])): res += eq[i] * aprox[-1][i]
        print (f'{res} = {eq[-1]}, abs = {abs(res - eq[-1])}')
        
    print()
