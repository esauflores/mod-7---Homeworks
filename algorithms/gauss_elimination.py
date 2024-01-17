
import numpy as np


def gauss_elimination(equations, process = False):
    n = len(equations); eq = equations.copy()

    if process: print_equations(eq)

    for i in range(n - 1):
        
        if eq[i][i] == 0:
            for j in range(i + 1, n):
                if eq[j][i] != 0:
                    eq[i], eq[j] = eq[j], eq[i]
                    break
        
        for j in range(i + 1, n):
            eq[j][-1] -= eq[i][-1] * eq[j][i] / eq[i][i]
            for k in range(n - 1, i - 1, -1):
                eq[j][k] -= eq[i][k] * eq[j][i] / eq[i][i]

        if process:
            print("Step:", i + 1)
            print_equations(eq)

    ans = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        t = sum([eq[i][j] * ans[j] for j in range(i + 1, n)])
        ans[i] = (eq[i][-1] - t) / eq[i][i]

    if process: print("Ans:", ans)

    return ans


def random_matrix(n):
    equations = [[np.random.random() for _ in range(n + 1)] for _ in range(n)]
    
    for i in range(n):
        equations[i][-1] = 0
        if equations[i][i] == 0: equations[i][i] = 1
        for j in range(n): equations[i][-1] += equations[i][j]
        
    return equations
        
def hilbert_matrix(n):
    A = np.zeros((n, n+1))
    for i in range(n):
        for j in range(n):
            A[i][j] = 1e6 / (i + j + 1)
     
    for i in range(n):
        A[i][-1] = 0
        for j in range(n): A[i][-1] += A[i][j]
            
    return A

def residual_error(x, equations):
    n, res = len(x), 0
    
    for i in range(n):
        t = 0
        for j in range(n): t += equations[i][j] * x[j]
        res += (t - equations[i][-1]) ** 2
    
    return res

def absolute_error(x0, x1):
    dist, n = 0, len(x0)
    for i in range(n): dist += (x1[i] - x0[i]) ** 2
    return dist ** 0.5
    
    
def check_ans(equations, ans, tol=1e-6):
    n = len(equations)
    for i in range(n):
        res = 0
        for j in range(n): res += equations[i][j] * ans[j]
        if abs(res - equations[i][-1]) >= tol: return False
    return True


def print_equations(equations):
    print()
    n = len(equations)
    for i in range(n):
        for j in range(n):
            print(f'{equations[i][j]}x{j}', end=' ')
            if j < n - 1: print('+', end=' ')
        print('=', equations[i][-1])
    print()
