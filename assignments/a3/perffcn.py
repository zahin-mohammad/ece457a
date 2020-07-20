from control import TransferFunction, feedback, step_info, step_response, series

# Credit to Nick Shields for creating the python implementation of the matlab code


def q1_perfFNC(Kp, Ti, Td):
    G = Kp * TransferFunction([Ti * Td, Ti, 1], [Ti, 0])
    F = TransferFunction(1, [1, 6, 11, 6, 0])
    sys = feedback(series(G, F), 1)
    sysinf = step_info(sys)

    t = []
    i = 0
    while i < 100:
        t.append(i)
        i += 0.01

    T, y = step_response(sys, T=t)

    ISE = sum((y - 1) ** 2)
    t_r = sysinf['RiseTime']
    t_s = sysinf['SettlingTime']
    M_p = sysinf['Overshoot']

    return ISE, t_r, t_s, M_p


if __name__ == '__main__':
    print(q2_perfFNC(10, 8, 2.3))
