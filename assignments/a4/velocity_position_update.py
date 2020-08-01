
import numpy as np
import math


def inertia_velocity(
    w,
    c1, c2,
):
    def f(particle, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        n_velocity = w*particle.velocity \
            + c1*r1*(particle.p_best - particle.position) \
            + c2*r2*(global_best - particle.position)
        n_position = particle.position + n_velocity

        return n_velocity, n_position

    return f


def constriction_velocity(
    c1, c2,
):
    assert c1 + c2 > 4.0, f"c1={c2} + c1={c1} < 4.0"
    k = 2 / (abs(2 - c1 - c2 - math.sqrt((c1+c2)**2 - 4*(c1+c2))))

    def f(particle, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        n_velocity = k*(particle.velocity
                        + c1*r1*(particle.p_best - particle.position)
                        + c2*r2*(global_best - particle.position))
        n_position = particle.position + n_velocity

        return n_velocity, n_position

    return f


def simple_velocity(
    c1, c2
):
    def f(particle, global_best):
        r1, r2 = np.random.uniform(0, 1, 2)
        n_velocity = particle.velocity \
            + c1*r1*(particle.p_best - particle.position) \
            + c2*r2*(global_best - particle.position)
        n_position = particle.position + n_velocity

        return n_velocity, n_position

    return f


def guaranteed_convergence_velocity(
    w,
    c1, c2,
    rho,
):
    def f(particle, global_best):
        if particle.position != global_best:
            return simple_velocity(
                c1, c2)(particle, global_best)
        r2 = np.random.uniform()
        n_velocity = w*particle.velocity + rho*(1-2*r2)
        n_position = global_best + w*particle.velocity + rho*(1-2*r2)

        return n_velocity, n_position

    return f
