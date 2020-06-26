import numpy as np
from random import randint


class State:
    def __init__(self, vehicle_count, locations, D, S, state=None):
        self.__vehicle_count = vehicle_count
        self.__locations = locations
        self.__D = D
        self.__S = S
        # TODO: Maybe try starting with a random state every time
        self.__state = state or (
            [1] + locations[1:] + [1 for _ in range(vehicle_count - 1)]) + [1]

    def __str__(self):
        state_str = str(self.__state)
        cost = self.get_cost()

        return f'''
State:
{state_str}\n
Cost: {cost}\n\n
        '''

    def copy(self, new_state=None):
        return State(
            self.__vehicle_count,
            self.__locations,
            self.__D,
            self.__S,
            new_state or self.__state
        )

    def get_neighbor(self, repeat=1):
        n = len(self.__state)

        state_copy = self.__state.copy()

        for _ in range(repeat):
            # Route HAS to start at a depot and end at a depot
            i, j = randint(1, n-2), randint(1, n-2)

            state_copy[i], state_copy[j] = state_copy[j], state_copy[i]

        return self.copy(state_copy)

    def get_cost(self):
        def compute_move_cost(i, j):
            return self.__D(i, j) + self.__S(j)

        cost = 0

        for i in range(len(self.__state) - 1):
            cost += compute_move_cost(self.__state[i], self.__state[i+1])

        return cost
