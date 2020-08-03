import math

# from nodes import Terminal
VARS = ["a0", "a1", "d0", "d1", "d2", "d3"]
all_binary_strings = ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111', '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111', '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111', '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111',
                      '100000', '100001', '100010', '100011', '100100', '100101', '100110', '100111', '101000', '101001', '101010', '101011', '101100', '101101', '101110', '101111', '110000', '110001', '110010', '110011', '110100', '110101', '110110', '110111', '111000', '111001', '111010', '111011', '111100', '111101', '111110', '111111']


def max_program_depth(program):
    def dfs(n, depth):
        if isinstance(n.children[0], str):
            return depth + 1
        return max([
            dfs(c, depth+1) for c in n.children
        ])
    return dfs(program, 0)


def fitness(program):
    if max_program_depth(program) > 8:
        return 0
    correct = 0

    for binary_string in all_binary_strings:
        inputs = {var: int(c) for var, c in zip(VARS, binary_string)}
        if bool(result(**inputs)) == program.evaluate(inputs):
            correct += 1

    return correct/len(all_binary_strings)


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


if __name__ == "__main__":
    print({var: int(c) for var, c in zip(VARS, "000000")})
