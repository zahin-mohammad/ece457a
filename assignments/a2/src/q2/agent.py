from board import *


class Agent:
    def __init__(self, name):
        self.name = name

    def get_next_states(self, board: Board):
        return board.next_moves()
