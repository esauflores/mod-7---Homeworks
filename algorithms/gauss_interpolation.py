
import algorithms.gauss_elimination as gauss
import algorithms.polynomial as poly
import numpy as np

def gauss_interpolation(x, y):
    n = len(x)
    matrix = [[1 for _ in range(n + 1)] for _ in range(n)]
    
    for i in range(n):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j - 1] * x[i]
        matrix[i][-1] = y[i]
        
    ans = gauss.gauss_elimination(matrix)
    
    return ans

def plot(axs, x_knots, y_knots, l, r, n = 100, color = 'red', point_color = 'green'):
    f = gauss_interpolation(x_knots, y_knots)
    x = np.linspace(l, r, n)
    y = [poly.polynomial(i, f) for i in x]
    
    axs.scatter(x_knots, y_knots, color=point_color)
    axs.plot(x, y, color=color, label='Gauss interpolation')

    axs.legend(axs.get_legend_handles_labels()[0], axs.get_legend_handles_labels()[1], loc='upper left')
