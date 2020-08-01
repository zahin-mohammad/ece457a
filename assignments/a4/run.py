from particle_swarm_optimization import simulation
from fitness import six_hump_camelback
from particle import Particle
from velocity_update import *


c1 = c2 = 2.05


def termination_condition(iteration_count: int):
    def f():
        for i in range(iteration_count):
            yield i
    return f


x_y_range = (-5.0, 5.0)
particles = [
    Particle(x_y_range, x_y_range) for i in range(100)
]


v_update_fn = constriction_velocity(c1, c2)

avg_best, best = simulation(
    termination_condition=termination_condition(10000),
    particles=particles,
    fitness_function=six_hump_camelback,
    velocity_update=v_update_fn
)

# print(np.array(best))
