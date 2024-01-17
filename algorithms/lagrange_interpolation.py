import numpy as np

def lagrangian_multiplier(x, x_knots, i):
    result = 1
    for j in range(len(x_knots)):
        if i != j: result *= (x - x_knots[j]) / (x_knots[i] - x_knots[j])
        
    return result

def lagrange_interpolation(x, x_knots, y_knots):
    result = 0
    for i in range(len(x_knots)):
        result += y_knots[i] * lagrangian_multiplier(x, x_knots, i)

    return result

def plot(axs, x_knots, y_knots, l, r, n = 100, color = 'blue', point_color = 'green'):
    x = np.linspace(l, r, n)
    y = [lagrange_interpolation(i, x_knots, y_knots) for i in x]
    
    axs.scatter(x_knots, y_knots, color=point_color)
    axs.plot(x, y, color=color, label='Lagrange interpolation')
    axs.legend(axs.get_legend_handles_labels()[0], axs.get_legend_handles_labels()[1], loc='upper left')
    