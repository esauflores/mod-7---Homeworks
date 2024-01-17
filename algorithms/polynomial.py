def polynomial(x, coeff):
    result, t = 0, 1
    for i in range(len(coeff)):
        result += coeff[i] * t
        t *= x
    return result