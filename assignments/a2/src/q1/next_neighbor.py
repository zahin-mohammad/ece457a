from random import random
from util import clip_output_to_interval
from easom import INTERVAL


@clip_output_to_interval(*INTERVAL)
def next_neighbor(x, T, T_initial):
    x1, x2 = x

    def move(xi):
        amplitude = (max(INTERVAL) - min(INTERVAL)) * (T / T_initial)
        delta = (-amplitude / 2) + amplitude * random()

        return xi + delta

    return (move(x1), move(x2))
