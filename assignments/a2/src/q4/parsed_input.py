import numpy as np
from math import sqrt

problem = 'A-n39-k6.vrp'


D_data = np.genfromtxt(problem, dtype=int,
                       skip_header=7, skip_footer=44)
depot_data = np.genfromtxt(
    problem, dtype=int, skip_header=47, skip_footer=4)


# Distance from i -> j
def D(i, j):
    x_i, y_i = D_data[i-1, 1], D_data[i-1, 2]
    x_j, y_j = D_data[j-1, 1], D_data[j-1, 2]

    dx = x_i - x_j
    dy = y_i - y_j

    return int(sqrt(dx**2 + dy**2))


# Service Time at i
def S(i):
    return depot_data[i-1, 1]


locations = [l for l, _ in depot_data]
