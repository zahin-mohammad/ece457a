from nodes import *
import numpy as np


class Individual:
    def __init__(self,
                 program=None,
                 max_depth=11):
        self.program = program
        max_depth = np.random.choice(range(2, max_depth))
        full_mode = max_depth % 2
        if self.program is None:
            self.program = random_node(
                depth=0,
                max_depth=max_depth,
                full_mode=full_mode
            )
        self.fitness = None
