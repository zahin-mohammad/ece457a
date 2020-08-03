from nodes import *
import numpy as np
from six_multiplexer import fitness


class Individual:
    def __init__(self, program=None, max_depth=None, f=None):
        self.program = program
        self.max_depth = max_depth

        self.full_mode = max_depth % 2
        if self.program is None:
            self.program = random_node(
                depth=0,
                max_depth=max_depth,
                full_mode=self.full_mode
            )
        self.fitness = f
        if self.fitness is None:
            self.fitness = fitness(self.program)

    def copy(self):
        return Individual(
            program=self.program.copy(),
            max_depth=self.max_depth,
            f=self.fitness
        )
