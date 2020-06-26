from agent import *
from board import *
from random import random
import numpy as np


class RandomAgent(Agent):
    def make_a_move(self, board: Board) -> Board:
        available_moves = self.get_next_states(board)
        moves = np.array(list(available_moves))
        return np.random.choice(moves)
