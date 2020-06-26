from random import uniform
from easom import INTERVAL


def get_random_state():
    x1 = uniform(*INTERVAL)
    x2 = uniform(*INTERVAL)

    return (x1, x2)
