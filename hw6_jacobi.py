import algorithms.jacobi as jac

# Test 1

# jac.jacobi([[5, 1, 1, 7], [1, 4, -1, 4], [1, 2, 5, 8]], 1e-6, 100, True)


# Test 2
jac.jacobi(jac.diagonal_dominant_matrix(3), 1e-6, 100, True)