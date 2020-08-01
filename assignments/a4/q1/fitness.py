# z = (4 − 2.1*x² + x⁴/3)*x² + x*y + ( −4 + 4*y²)*y²
def six_hump_camelback(x, y):
    a = (4 - 2.1 * (x ** 2) + (x ** 4)/3) * (x ** 2)
    b = (x * y)
    c = (-4 + 4 * (y ** 2)) * (y ** 2)
    return a + b + c
