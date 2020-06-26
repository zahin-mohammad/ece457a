from agent import *
from board import *
from minimax import *
from directions import *
# from random import random
import numpy as np


# TODO: FIX LOOPSSSS!!!
class AIAgent(Agent):
    @staticmethod
    def get_children(node: (str, int)):
        board = Board(*node)

        for child in board.next_moves():
            if child is not None:
                yield child.serialize()
    '''
    1. How many cells do you control (this is an indication of proces vs goal)
    2. How many oponent cells are trapped
    3. Can we split next move? 
    '''

    @staticmethod
    def evaluate1(node: (str, str)):
        board = Board(*node)

        sum_positive_values = board.is_whites_turn()

        count = 0
        for x in range(1, 5):
            for y in range(1, 5):
                if sum_positive_values and board.get(x, y) > 0:
                    count += 1

                elif (not sum_positive_values) and board.get(x, y) < 0:
                    count += 1

        return count

    @staticmethod
    def evaluate2(node: (str, str)):
        my_node_count = AIAgent.evaluate1(node)
        # my_node_count = 0

        board = Board(*node)
        sum_positive_values = board.is_whites_turn()

        num_opponent_blocks = 0
        for x in range(1, 5):
            for y in range(1, 5):
                cell = board.get(x, y)

                if sum_positive_values and cell < 0:
                    for dx, dy in direction.DIRECTIONS:
                        neighbor = board.get(x + dx, y + dy)
                        if (x+dx == y + dy == 1) or (x+dx == y + dy == 4) or (x + dx == 1 and y+dy == 4) or (x+dx == 4 and y+dy == 1):
                            num_opponent_blocks += 350
                        elif neighbor is None:
                            num_opponent_blocks += 1
                        elif neighbor > 0:
                            num_opponent_blocks += 1

                elif (not sum_positive_values) and cell > 0:
                    for dx, dy in direction.DIRECTIONS:
                        neighbor = board.get(x + dx, y + dy)
                        if (x+dx == y + dy == 1) or (x+dx == y + dy == 4) or (x + dx == 1 and y+dy == 4) or (x+dx == 4 and y+dy == 1):
                            num_opponent_blocks += 350
                        elif neighbor is None:
                            num_opponent_blocks += 1
                        elif neighbor < 0:
                            num_opponent_blocks += 1

        # TODO: Return
        return 0.75 * num_opponent_blocks + 0.0 * my_node_count

    @staticmethod
    def evaluate3(node: (str, str)):
        num_opponent_blocks = AIAgent.evaluate2(node)

        board = Board(*node)
        my_node_count = 0
        opponent_node_count = 0

        i_am_white = board.is_whites_turn()

        for x in range(1, 5):
            for y in range(1, 5):
                cell = board.get(x, y)

                if i_am_white:
                    if cell > 0:
                        my_node_count += 1
                    elif cell < 0:
                        opponent_node_count += 1

                else:
                    # I am black
                    if cell < 0:
                        my_node_count += 1
                    elif cell > 0:
                        opponent_node_count += 1

        return my_node_count - opponent_node_count + num_opponent_blocks

    '''
    Generate game tree to specified depths
    Root: is Max
    White will try to maximize whites nodes
    Black will try to minimize black nodes
    '''

    def __init__(self, *args):
        super(AIAgent, self).__init__(*args)
        self.minimax = configure_minimax(
            AIAgent.evaluate3, AIAgent.get_children)

    def make_a_move(self, board: Board) -> Board:
        next_moves = self.minimax(board.serialize())

        best_move_cost, _ = max(next_moves, key=lambda x: x[0])

        best_moves = [Board(*node) for cost,
                      node in next_moves if cost == best_move_cost]

        return np.random.choice(np.array(best_moves))
