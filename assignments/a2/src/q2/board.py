import numpy as np
from colors import *
from directions import *


def DEFAULT_START_STATE():
    return '10 0 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 -10'


# TODO: Implement reverse_move as well if required
class Board:

    @staticmethod
    def _new_position(position, direction):
        return (position[0] + direction[0], position[1] + direction[1])

    # In the function below, we don't assert for out of bounds because we need it to clip the value at the bounds if it goes beyond
    @staticmethod
    def add(val, incr, source):
        incr = abs(incr)
        ret = None
        if source > 0:
            ret = val + incr
            return min(10, ret)
        else:
            ret = val - incr
            return max(-10, ret)

    # In the function below, we don't assert for out of bounds because we need it to clip the value at the bounds if it goes beyond
    @staticmethod
    def remove(val, decr, source):
        decr = abs(decr)
        ret = None
        if source > 0:
            ret = val - decr
            return max(0, ret)
        else:
            ret = val + decr
            return min(0, ret)

    def __init__(self, state=DEFAULT_START_STATE(), t=0):
        self.__state = np.matrix(state)
        self.__t = int(t)

    def __str__(self):
        return str(self.__state)

    def serialize(self):
        sb = []
        for i in range(4):
            for j in range(4):
                sb.append(str(self.__state[i, j]) + ' ')
            sb.append('; ')

        return (''.join(sb[:-1]), self.__t)

    def get(self, x, y):
        if not (1 <= x <= 4 and 1 <= y <= 4):
            # Out of bounds
            return None

        return self.__state[4-y, x-1]

    def set(self, x, y, value):
        if not (1 <= x <= 4 and 1 <= y <= 4):
            # Out of bounds
            return False

        self.__state[4-y, x-1] = value
        return True

    def print(self):
        for i in range(4):
            for j in range(4):
                color = colors.BLUE
                num = self.__state[i, j]

                if num > 0:
                    color = colors.GREEN
                elif num < 0:
                    color = colors.RED
                    num = -num

                if num == 10:
                    num = 'X'

                print(f'{color}{num}', end=' ')

            print()

        print(colors.ENDC)

    def __is_positives_turn(self):
        # Positive moves first
        return self.__t % 2 == 0

    def is_whites_turn(self):
        return self.__is_positives_turn()

    def __is_same_player(self, player_position, new_position):
        return self.get(*player_position) != 0 and self.get(*new_position) != 0 and self.get(*player_position) * self.get(*new_position) > 0

    def __is_free_or_mine(self, player_position, new_position):
        return self.get(*new_position) is not None and (self.get(*new_position) == 0 or self.__is_same_player(player_position, new_position))

    def __get_valid_new_positions(self, position, direction):
        new_positions = []

        new_position = None
        for _ in range(3):
            new_position = Board._new_position(
                new_position or position, direction)

            if self.__is_free_or_mine(position, new_position):
                new_positions.append(new_position)
            else:
                break

        return new_positions

    def __generate_board_after_move(self, position, direction):
        # 4 Main Cases

        # 1. position + direction is taken or out of bounds
        # 2. position + direction*2 is taken or out of bounds
        # 3. position + direction*3 is taken or out of bounds
        # 4. Free

        valid_new_positions = self.__get_valid_new_positions(
            position, direction)

        if len(valid_new_positions) == 0:
            return None

        new_state = np.copy(self.__state)

        new_board = Board(new_state, self.__t + 1)
        # Since by this point, there is a valid move - set current cell to 0
        new_board.set(*position, 0)

        third_incr = 0
        source_val = self.get(*position)
        if len(valid_new_positions) == 3:
            new_pos_incr = abs(Board.remove(
                self.get(*position), 3, source_val))

            new_pos_val = Board.add(
                self.get(*valid_new_positions[2]), new_pos_incr, source_val)

            new_board.set(
                *(valid_new_positions[2]), new_pos_val)

            third_incr = new_pos_incr

        second_incr = 0
        if len(valid_new_positions) >= 2:
            new_pos_incr = 0
            if third_incr == 0:
                new_pos_incr = abs(Board.remove(
                    self.get(*position), 1, source_val))
            else:
                # TODO: Remove commented block if there's no error after testing
                # remaining_val = Board.remove(
                #     self.get(*position), third_incr, source_val)
                # new_pos_incr = abs(Board.remove(remaining_val, 1, source_val))
                new_pos_incr = 2

            new_pos_val = Board.add(
                self.get(*(valid_new_positions[1])), new_pos_incr, source_val)

            new_board.set(*(valid_new_positions[1]), new_pos_val)

            second_incr = new_pos_incr

        if len(valid_new_positions) >= 1:
            # Add everything from old pos here if there is nothing after
            other_incr = third_incr + second_incr
            new_pos_incr = abs(Board.remove(
                self.get(*position), other_incr, source_val))

            new_pos_val = Board.add(
                self.get(*(valid_new_positions[0])), new_pos_incr, source_val)

            new_board.set(*(valid_new_positions[0]), new_pos_val)

        return new_board

    def next_moves(self):
        # Generator function that generates the next possible moves one by one
        def is_not_zero(x, y):
            return self.get(x, y) != 0

        def is_my_chance(x, y):
            return (self.__is_positives_turn() and self.get(x, y) > 0) or ((not self.__is_positives_turn()) and self.get(x, y) < 0)

        no_moves_made = True
        for x in range(1, 5):
            for y in range(1, 5):
                if is_not_zero(x, y) and is_my_chance(x, y):
                    for dir in direction.DIRECTIONS:
                        new_board = self.__generate_board_after_move(
                            (x, y), dir)

                        if new_board is not None:
                            no_moves_made = False
                            yield new_board

        if no_moves_made:
            yield None


if __name__ == '__main__':
    board = Board()
    next_moves = board.next_moves()

    print("Current Board:")
    print()
    board.print()
    print()
    print()

    print("Possible Next Moves")
    for i, next_board in enumerate(next_moves):
        print(f'Move #{i + 1}')
        print()
        next_board.print()
        print()
        print()
