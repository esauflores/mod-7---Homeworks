
import algorithms.bisection as bis
import algorithms.fixed_point as fix
import algorithms.newton as new
import numpy as np
import matplotlib.pyplot as plt

# Test 1
# t, x, alpha = 3, [0, -1.5, 4.5], [0.1, 1e-6, 1e-6]
# a, b = -2, 5
# f = lambda x: (x - 1) * (x + 1) * (x - 3)
# df = lambda x: 3 * x**2 - 6 * x - 1
# maxsteps = 100


# Test 2
# t, x, alpha = 2, [0, 1], [1, 1e-6]
# a, b = -2, 2
# f = lambda x: 2*np.sin(x) - x
# df = lambda x: 2*np.cos(x)
# maxsteps = 100

# Test 3
t, x, alpha = 3, [-1, 0.1, 4.5], [1e-6, 1e-3, 0.1]
a, b = -1, 1
f = lambda x: 1 - np.exp(-x)
df = lambda x: np.exp(-x)
maxsteps = 100


fig, axs = plt.subplots(1, t, figsize=(14, 14 / t))

# bisection
print("bisection: ")
a1, b1, root, steps, aprox = bis.bisection(a, b, f, 1e-6, maxsteps, True)
for i in range(t): bis.plot(axs[i], aprox)

# fixed point
print("fixed point: ")
for i in range(t):
    root, steps, aprox = fix.fixed_point(x[i], f, alpha[i], 1e-6, maxsteps, True)
    fix.plot(axs[i], aprox)

# newton
print("newton: ")
for i in range(t):
    root, steps, aprox = new.newton(x[i], f, df, 1e-6, maxsteps, True)
    new.plot(axs[i], aprox)

# log scale

for i in range(t):
    axs[i].set_yscale("log")
    axs[i].set_xlabel("steps")
    axs[i].set_ylabel("error")
    axs[i].set_title("x = {} a = {} b = {} alpha = {}".format(x[i], a, b, alpha[i]))
    axs[i].legend()
    
fig.tight_layout()
plt.show()
