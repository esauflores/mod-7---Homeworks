import algorithms.gauss_elimination as gauss
import matplotlib.pyplot as plt
import numpy as np


x = [i for i in range(2, 100)]
y_residual_random = [0 for i in range(2, 100)]
y_residual_hilbert = [0 for i in range(2, 100)]

y_residual_random_numpy = [0 for i in range(2, 100)]
y_residual_hilbert_numpy = [0 for i in range(2, 100)]

for i in range(2, 100):
    res = [1 for _ in range(i)]
    # random matrix
    random_matrix = gauss.random_matrix(i)
    ans = gauss.gauss_elimination(random_matrix.copy(), False)
    y_residual_random[i - 2] = gauss.residual_error(ans, random_matrix.copy())
    
    # hilbert matrix
    hilbert_matrix = gauss.hilbert_matrix(i)
    ans = gauss.gauss_elimination(hilbert_matrix.copy(), False)
    y_residual_hilbert[i-2] = gauss.residual_error(ans, hilbert_matrix.copy())
    
    # numpy.linalg.solve random matrix
    a = [[random_matrix[i2][j2] for j2 in range(i)] for i2 in range(i)]
    b = [random_matrix[i2][-1] for i2 in range(i)]
    ans = np.linalg.solve(a, b)
    y_residual_random_numpy[i - 2] = gauss.residual_error(ans, random_matrix)
    
    # numpy.linalg.solve hilbert matrix
    a = [[hilbert_matrix[i2][j2] for j2 in range(i)] for i2 in range(i)]
    b = [hilbert_matrix[i2][-1] for i2 in range(i)]
    ans = np.linalg.solve(a, b)
    y_residual_hilbert_numpy[i - 2] = gauss.residual_error(ans, hilbert_matrix)
    
  
y_residual_random = [ (i if i != 0.0 else 1e-50) for i in y_residual_random]
y_residual_hilbert = [ (i if i != 0.0 else 1e-50) for i in y_residual_hilbert]
y_residual_random_numpy = [ (i if i != 0.0 else 1e-50) for i in y_residual_random_numpy]
y_residual_hilbert_numpy = [ (i if i != 0.0 else 1e-50) for i in y_residual_hilbert_numpy]
    
plt.plot(x, y_residual_random, label="random matrix", color="red")
plt.plot(x, y_residual_hilbert, label="hilbert matrix", color="blue")
plt.plot(x, y_residual_random_numpy, label="random matrix numpy", color="green")
plt.plot(x, y_residual_hilbert_numpy, label="hilbert matrix numpy", color="purple")

plt.legend(["random matrix", "hilbert matrix", "random matrix numpy", "hilbert matrix numpy"], loc="upper right")
plt.xlabel("n")
plt.ylabel("residual error")

# log scale

plt.yscale("log")
plt.xscale("log")

plt.show()