import algorithms.spline_interpolation as spline
import matplotlib.pyplot as plt

# # Test 1

# coord = [(0, 1), (2, 2), (1, 4), (3, 4), (4, 1)]
# sorted_coord = sorted(coord)
# x = [i[0] for i in sorted_coord]
# y = [i[1] for i in sorted_coord]

# coeffs = spline.cubic_spline_coeffs(x, y)
# spline.plot(plt, -10, 10, coeffs, x, y, 10000)


# Test 2

coord = [(0, 3), (2, 1), (1, 2), (3, 5), (4, 0)]
sorted_coord = sorted(coord)
x = [i[0] for i in sorted_coord]
y = [i[1] for i in sorted_coord]

coeffs = spline.cubic_spline_coeffs(x, y)
spline.plot(plt, -10, 10, coeffs, x, y, 10000)


# limit plot view in x axis
plt.xlim(-10, 10)

# limit plot view in y axis
plt.ylim(-10, 10)

plt.grid()

plt.show()