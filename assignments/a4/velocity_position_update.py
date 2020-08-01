
import numpy as np
import math

'''
    Each velocity_position_update fn is 3 layers:
    layer 1: simulation params
    layer 2: simulation iteration data
    layer 3: particle data
'''


def inertia_velocity(
    w,
    c1, c2,
):
    def f1(num_failure, num_success, global_best):
        def f2(p_v, p_pos, p_best):
            r1, r2 = np.random.uniform(0, 1, 2)
            n_velocity = w*p_v \
                + c1*r1*(p_best - p_pos) \
                + c2*r2*(global_best - p_pos)
            n_position = p_pos + n_velocity
            return n_velocity, n_position
        return f2
    return f1


def constriction_velocity(
    c1, c2,
):
    assert c1 + c2 > 4.0, f"c1={c2} + c1={c1} < 4.0"
    k = 2 / (abs(2 - c1 - c2 - math.sqrt((c1+c2)**2 - 4*(c1+c2))))

    def f1(num_failure, num_success, global_best):
        def f2(p_v, p_pos, p_best):
            r1, r2 = np.random.uniform(0, 1, 2)
            n_velocity = k*(p_v
                            + c1*r1*(p_best - p_pos)
                            + c2*r2*(global_best - p_pos))
            n_position = p_pos + n_velocity
            return n_velocity, n_position
        return f2
    return f1


def simple_velocity(
    c1, c2
):
    def f1(num_failure, num_success, global_best):
        def f2(p_v, p_pos, p_best):
            r1, r2 = np.random.uniform(0, 1, 2)
            n_velocity = p_v \
                + c1*r1*(p_best - p_pos) \
                + c2*r2*(global_best - p_pos)
            n_position = p_pos + n_velocity
            return n_velocity, n_position
        return f2
    return f1


def guaranteed_convergence_velocity(
    w,
    c1, c2,
):
    rhos = [1.0]
    e_s = 15
    e_f = 5

    def f1(num_failure, num_success, global_best):
        rho = None
        if len(rhos) == 1:
            rho = rhos[-1]
        elif num_success > e_s:
            rhos.append(2*rhos[-1])
            rho = rhos[-1]
        elif num_failure > e_f:
            rhos.append(0.5*rhos[-1])
            rho = rhos[-1]
        else:
            rhos.append(rhos[-1])
            rho = rhos[-1]

        def f2(p_v, p_pos, p_best):
            if tuple(p_pos) != tuple(global_best):
                return simple_velocity(
                    c1, c2)(num_failure, num_success, global_best)(p_v, p_pos, p_best)
            r2 = np.random.uniform()
            n_velocity = w*p_v + rho*(1-2*r2)
            n_position = global_best + w*p_v + rho*(1-2*r2)
            return n_velocity, n_position
        return f2
    return f1
