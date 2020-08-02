import math

VARS = ["a0", "a1", "d0", "d1", "d2", "d3"]


def fitness(individual):
    all_binary_strings = generate_binary_strings(len(VARS))

    correct = 0
    total = 0

    for binary_string in all_binary_strings:
        inputs = {var: int(c) for var, c in zip(VARS, binary_string)}
        if result(**inputs) == individual.program.evaluate(inputs):
            correct += 1
        total += 1
    individual.fitness = correct/total
    return individual.fitness


def generate_binary_strings(n):
    # Credit to: https://gist.github.com/kevinwuhoo/2424597

    # 2^(n-1)  2^n - 1 inclusive
    bin_arr = range(0, int(math.pow(2, n)))
    bin_arr = [bin(i)[2:] for i in bin_arr]

    # Prepending 0's to binary strings
    max_len = len(max(bin_arr, key=len))
    bin_arr = [i.zfill(max_len) for i in bin_arr]

    return bin_arr


def result(a0, a1, d0, d1, d2, d3):
    six_multiplexer_map = {
        0: {
            0: d0,
            1: d1,
        },
        1: {
            0: d2,
            1: d3
        }
    }
    return six_multiplexer_map[a0][a1]
