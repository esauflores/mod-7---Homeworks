import algorithms.fixed_point as fix


# Test 1
root, steps, aprox = fix.fixed_point(1.5, lambda x: x**2-4, 0.5, 1e-6, 1e6, True)


# Test 2    
root, steps, aprox = fix.fixed_point(1.2, lambda x: x**2-4, 0.01, 1e-6, 1e6, True)


# Test 3
root, steps, aprox = fix.fixed_point(0.5, lambda x: x**2-4, 1e-5, 1e-6, 1e6, True)


# Test 4
root, steps, aprox = fix.fixed_point(0.5, lambda x: x**2-4, 1e-5, 1e-6, 1e6, True)


# Test 5
root, steps, aprox = fix.fixed_point(0.5, lambda x: x**2-4, 1e-8, 1e-6, 1e6, True)


# Test 6
root, steps, aprox = fix.fixed_point(1.5, lambda x: x**2-4, 0.2, 1e-3, 1e6, True)
