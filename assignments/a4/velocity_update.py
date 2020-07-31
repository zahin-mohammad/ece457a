
import numpy as np
import math


def inertia_velocity(
    w,
    c1, c2,
    r1, r2,
):
    def f(particle, global_best):
        return w*particle.velocity \
            + c1*r1*(particle.p_best - particle.position) \
            + c2*r2*(global_best - particle.position)
    return f


def constriction_velocity(
    c1, c2,
    r1, r2
):
    assert c1+c2 > 4.0, "c1 + c1 < 4.0"

    def f(particle, global_best):
        k = 2/(abs(2-c1-c2-math.sqrt((c1+c2)**2 - 4*(c1+c2))))

        return k*(particle.velocity
                  + c1*r1*(particle.p_best - particle.position)
                  + c2*r2*(global_best - particle.position))

    return f
