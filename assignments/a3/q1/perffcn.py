from control import TransferFunction, feedback, step_info, step_response, series

# Credit to Nick Shields for creating the python implementation of the matlab code

t = [i/100 for i in range(0, 10000)]
F = TransferFunction(1, [1, 6, 11, 6, 0])


def q1_perfFNC(Kp, Ti, Td):
    G = Kp * TransferFunction([Ti * Td, Ti, 1], [Ti, 0])
    sys = feedback(series(G, F), 1)
    sysinf = step_info(sys)

    T, y = step_response(sys, T=t)
    # return ISE, t_r, t_s, M_p
    return sum((y - 1) ** 2), sysinf['RiseTime'], sysinf['SettlingTime'], sysinf['Overshoot']


if __name__ == '__main__':
    print(q2_perfFNC(10, 8, 2.3))
