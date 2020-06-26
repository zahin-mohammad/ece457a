import numpy as np
from utils import *
from tabu_search import *

distance = np.genfromtxt('distance.csv', delimiter=',')
flow = np.genfromtxt('flow.csv', delimiter=',')


def gen_stopping_condition(max_iter):
    def stop():
        for _ in range(max_iter):
            yield False

    def gen_should_stop(iter):
        def should_stop():
            return next(iter, True)

        return should_stop

    return gen_should_stop(stop())


def evaluate(s, frequency=0):
    s = deserialize(s)
    sum = 0.0

    for i in range(20):
        for j in range(i + 1, 20):
            d_i, d_j = s[i], s[j]

            sum += flow[d_i, d_j] * distance[i, j]

    return -sum-frequency*2


def get_neighbors(s):
    s_copy = deserialize(s)
    n = s_copy.size

    for i in range(n):
        for j in range(i + 1, n):
            s_copy[i], s_copy[j] = s_copy[j], s_copy[i]
            yield serialize(s_copy)
            s_copy[i], s_copy[j] = s_copy[j], s_copy[i]


if __name__ == '__main__':
    for tabu_list_size in [5]:
        # initial_state = np.arange(20)
        # BEST STATE: 17, 5, 7, 1, 6, 19, 15, 20, 8, 13, 4, 2, 12, 11, 16, 18, 14, 10, 3, 9

        # TRIAL 1: INPUT: 6 2 3 19 10 11 15 1 12 18 16 17 5 8 7 13 14 4 0 9 => OUTPUT: 1287.0
        initial_state = deserialize(
            '15 6 11 7 10 5 0 13 16 18 9 14 17 2 12 19 3 8 4 1')

        # initial_state = np.array(list(map(
        #     lambda x: x-1, [17, 7, 5, 1, 6, 4, 20, 8, 11, 13, 19, 15, 12, 10, 16, 18, 2, 14, 3, 9])))
        # initial_state = np.array(
        #     list(map(lambda x: x-1, [2, 9, 8, 12, 1, 7, 11, 19, 13, 10, 5, 18, 3, 17, 14, 15, 6, 16, 20, 4])))
        # np.random.shuffle(initial_state)
        initial_state = serialize(initial_state)

        stopping_condition = gen_stopping_condition(500)

        tabu_search = configure_tabu_search(
            stopping_condition, get_neighbors, evaluate, tabu_list_size)

        print(f'Tabu List Size: {tabu_list_size}')
        print(f'Initial State: {initial_state}')
        print(f'Initial Cost: {-evaluate(initial_state)}')
        final_state = tabu_search(initial_state)
        print(f'Final State: {final_state}')
        print(f'Final Cost: {-evaluate(final_state)}')
        print()
