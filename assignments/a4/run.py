from particle_swarm_optimization import simulation
from fitness import six_hump_camelback
from particle import Particle
from velocity_position_update import *


x_y_range = (-5.0, 5.0)
particles = [
    Particle(x_y_range, x_y_range) for i in range(100)
]


def termination_condition(iteration_count: int):
    def f():
        for i in range(iteration_count):
            yield i
    return f


c1 = c2 = 2.05
w = 0.5


simple_velocity_position_fn = simple_velocity(c1, c2)
inertia_velocity_position_fn = inertia_velocity(w, c1, c2)
constriction_velocity_position_fn = constriction_velocity(c1, c2)
guaranteed_convergence_velocity_position_fn = guaranteed_convergence_velocity(
    w, c1, c2, )

# inertia_velocity_fn = inertia_velocity()

avg_best, best = simulation(
    termination_condition=termination_condition(100),
    particles=particles,
    fitness_function=six_hump_camelback,
    velocity_position_update=guaranteed_convergence_velocity_position_fn
)
