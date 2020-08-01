
import numpy as np
import math


def inertia_velocity(
    w,
    c1, c2,
):
    def f(particle, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        return w*particle.velocity \
            + c1*r1*(particle.p_best - particle.position) \
            + c2*r2*(global_best - particle.position)
    return f


def constriction_velocity(
    c1, c2,

):
    assert c1 + c2 > 4.0, f"c1={c2} + c1={c1} < 4.0"
    k = 2 / (abs(2 - c1 - c2 - math.sqrt((c1+c2)**2 - 4*(c1+c2))))

    def f(p_v, p_pos, p_best, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        return k*(p_v
                  + c1*r1*(p_best - p_pos)
                  + c2*r2*(global_best - p_pos))

    return f


def simple_velocity(
    c1, c2
):
    def f(particle, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        return particle.velocity \
            + c1*r1*(particle.p_best - particle.position) \
            + c2*r2*(global_best - particle.position)
    return f
