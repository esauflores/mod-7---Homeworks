import algorithms.lagrange_interpolation as lag
import matplotlib.pyplot as plt
import numpy as np

t = 3
fig, axs = plt.subplots(1, t, figsize=(14, 14 / t))

# Test 1
x = [0, 1, 2]
y = [1, 0, 1]
l, r = -4, 4

lag.plot(axs[0], x, y, l, r)

# Test 2
N = 2
l, r = -2, 2
x = np.linspace(l, r, N)
y = np.random.rand(N)

lag.plot(axs[1], x, y, l, r)

# Test 3
N = 4
l, r = -2, 2
x = np.linspace(l, r, N)
y = np.random.rand(N)

lag.plot(axs[2], x, y, l, r)


# show plot

fig.tight_layout()
plt.show()
