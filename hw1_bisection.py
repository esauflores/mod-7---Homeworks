import algorithms.bisection as bis


# Test 1  x^2 - 2
a, b, root, steps, aprox = bis.bisection(0, 7, lambda x: x**2-2, 1e-6, 100, True)

# Test 2  x^3 - x^2 - 1
a, b, root, steps, aprox = bis.bisection(-100, 100, lambda x: x**3-x**2 - 1, 1e-6, 100, True)
