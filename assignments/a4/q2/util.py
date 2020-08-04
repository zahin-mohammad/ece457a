import math
def generate_binary_strings(n):
    # Credit to: https://gist.github.com/kevinwuhoo/2424597

    # 2^(n-1)  2^n - 1 inclusive
    bin_arr = range(0, int(math.pow(2, n)))
    bin_arr = [bin(i)[2:] for i in bin_arr]

    # Prepending 0's to binary strings
    max_len = len(max(bin_arr, key=len))
    bin_arr = [i.zfill(max_len) for i in bin_arr]

    return bin_arr

if __name__ == "__main__":
    print(generate_binary_strings(11))