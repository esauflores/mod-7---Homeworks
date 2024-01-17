import algorithms.combined as com


# Test 1
a, b, root, steps, aprox = com.combined(2, -1000, 1000, lambda x: (x-3)*(x-1)**2, lambda x: 3*x**2-10*x+7, 1e-6, 100, True)

# Test 2
a, b, root, steps, aprox = com.combined(-2, -1000, 1000, lambda x: (x-3)*(x-1)**2, lambda x: 3*x**2-10*x+7, 1e-6, 100, True)

# Test 3
a, b, root, steps, aprox = com.combined(-1, -1000, 1000, lambda x: (x-3)*(x-1)**2, lambda x: 3*x**2-10*x+7, 1e-6, 100, True)
