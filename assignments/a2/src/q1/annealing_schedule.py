from math import log, cos, pi


def make_annealing_schedule(get_next_T):
    def annealing_schedule(T_i, T_f, iter_per_T):
        t = 1
        T = get_next_T(T_f, T_i, t)

        while T > T_f:
            for _ in range(iter_per_T):
                yield T
            t += 1
            T = get_next_T(T_f, T_i, t)

    return annealing_schedule


def make_trigonometric_schedule(n):
    def T_k(T_n, T_0, k):
        if k == n:
            return T_n

        return T_n + (0.5) * (T_0 - T_n) * (1 + cos((k * pi) / n))

    return make_annealing_schedule(T_k)
