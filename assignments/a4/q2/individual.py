from nodes import *
import numpy as np
from six_multiplexer import VARS
from six_multiplexer import fitness
import random


class Individual:
    def __init__(self, max_depth=3):
        self.program = (np.random.choice(T_UNION_F))(0, max_depth)


if __name__ == "__main__":
    individual = Individual()
    inputs = {key: bool(random.getrandbits(1)) for key in VARS}
    print(inputs)
    print(individual.program.to_string())
    print(individual.program.evaluate(inputs))
    print(fitness(individual.program))
