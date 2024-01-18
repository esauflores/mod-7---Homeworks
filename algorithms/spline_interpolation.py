import numpy as np
# import algorithms.gauss_elimination as gauss
import algorithms.polynomial as poly

def cubic_spline_coeffs(x, y):  
    n = len(x) - 1
    eqs = [[0 for _ in range(4 * n)] for _ in range(4 * n)]
    res = [0 for _ in range(4 * n)]
  
    # first 2n equations
    # qi(xi) = yi
    # qi(xi+1) = yi+1
    
    pos = 0
    for i in range(n):
        eqs[pos][(4*i):(4*i+4)] = [1, x[i], x[i]**2, x[i]**3]; res[pos] = y[i]; pos += 1
        eqs[pos][(4*i):(4*i+4)] = [1, x[i+1], x[i+1]**2, x[i+1]**3]; res[pos] = y[i+1]; pos += 1
        
    # next 2n-1 equations
    # qi'(xi+1) = qi+1'(xi+1)
    # qi''(xi+1) = qi+1''(xi+1)
    for i in range(1, n):
        eqs[pos][(4*i-4):(4*i+4)] = [0, 1, 2*x[i], 3*x[i]**2, 0, -1, -2*x[i], -3*x[i]**2]; res[pos] = 0; pos += 1
        eqs[pos][(4*i-4):(4*i+4)] = [0, 0, 2, 6*x[i], 0, 0, -2, -6*x[i]]; res[pos] = 0; pos += 1

    # last 2 equations
    # q0''(x0) = 0
    # qn''(xn) = 0
    eqs[pos][0:4] = [0, 0, 2, 6*x[0]]; res[pos] = 0; pos += 1
    eqs[pos][(4*n-4):(4*n)] = [0, 0, 2, 6*x[n]]; res[pos] = 0; pos += 1
    
    ans = np.linalg.solve(eqs, res)
    
    coeffs = [[ans[i] for i in range(4*j, 4*j+4)] for j in range(n)]

    return coeffs


def cubic_spline(coeffs, x, x0):    
    if x0 <= x[1]: return poly.polynomial(x0, coeffs[0])
    if x0 >= x[-1]: return poly.polynomial(x0, coeffs[-1])
    
    for i in range(1, len(x)):
        if x0 <= x[i]: return poly.polynomial(x0, coeffs[i-1])
    
    
    # n, i = len(x), len(x)-2
    
    # pow2, powers = int(np.log2(n)), [1]
    # for _ in range(1, pow2+1): powers.append(2*powers[-1])
    
    # while pow2 >= 0:
    #     new = i - powers[pow2]
    #     if new >= 0 and x0 <= x[new]: i = new
    #     pow2 -= 1

    # print(x0, i)

    # return poly.polynomial(x0, coeffs[i])
    

def plot(axs, l, r, coeffs, x0, y0, n = 100):
    x = np.linspace(l, r, n)
    y = [cubic_spline(coeffs, x0, i) for i in x]
    axs.plot(x, y, color="red")
    # original points
    axs.scatter(x0, y0, color="green")
    