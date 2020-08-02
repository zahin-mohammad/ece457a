from nodes import *
import numpy as np


class Individual:
    def __init__(self,
                 program=None,
                 max_depth=8):
        self.program = program
        if self.program is None:
            self.program = (np.random.choice(T_UNION_F))(0, max_depth)
        self.fitness = None
