import numpy as np
np.random.seed(1)

import sys
from particle_swarm_optimization import simulation
from fitness import six_hump_camelback
from particle import Particle
from velocity_position_update import *
from plot import graph


x_y_range = (-5.0, 5.0)
iterations = 200
particle_count = 100


def termination_condition(iteration_count: int):
    def f():
        for i in range(iteration_count):
            yield i
    return f


'''
    Code a simple PSO to solve the problem. To do this you need to encode
    the problem, initialize a population, select a velocity update equation, and select a
    stopping criterion. Run your code and report: final solution, plot the progress of the
    average fitness and the best particle fitness.
'''


def q_one_one():
    c1 = c2 = 2.05

    swarm = [
        Particle(x_y_range, x_y_range) for i in range(100)
    ]
    velocity_position_fn = simple_velocity(x_y_range, x_y_range, c1, c2)

    avg_fit, best_fit, g_best = simulation(
        termination_condition=termination_condition(iterations),
        swarm=swarm,
        fitness_function=six_hump_camelback,
        velocity_position_update=velocity_position_fn
    )
    test = "Simple PSO"
    title = f"Fitness vs Iterations: {test}"
    data = [("Average Fitness", avg_fit)]
    data.append(("Best Fitness", best_fit))

    graph(title, data)
    print(test)
    print(f"\t c1: {c1}")
    print(f"\t c2: {c2}")
    print(f"\t iterations: {iterations}")
    print(f"\t particles: {particle_count}")
    print(f"\t best fitness: {six_hump_camelback(g_best[0],g_best[1])}")
    print(f"\t best x,y: {g_best[0]} {g_best[1]}")


'''
    Use the Inertia Weight version of velocity update equation with Global
    best. Run your code and report: final solution, and plot the progress of the average
    fitness of the population and the global best particle fitness
'''


def q_one_two():
    c1 = c2 = 2.05
    w = 0.5

    swarm = [
        Particle(x_y_range, x_y_range) for i in range(100)
    ]
    velocity_position_fn = inertia_velocity(x_y_range, x_y_range, w, c1, c2)

    avg_fit, best_fit, g_best = simulation(
        termination_condition=termination_condition(iterations),
        swarm=swarm,
        fitness_function=six_hump_camelback,
        velocity_position_update=velocity_position_fn
    )
    test = "Inertia Weight PSO"
    title = f"Fitness vs Iterations: {test}"
    data = [("Average Fitness", avg_fit)]
    data.append(("Best Fitness", best_fit))

    graph(title, data)
    print(test)
    print(f"\t c1: {c1}")
    print(f"\t c2: {c2}")
    print(f"\t w: {w}")
    print(f"\t iterations: {iterations}")
    print(f"\t particles: {particle_count}")
    print(f"\t best fitness: {six_hump_camelback(g_best[0],g_best[1])}")
    print(f"\t best x,y: {g_best[0]} {g_best[1]}")


'''
    Use Constriction Factor version of velocity update equation with Global Best.
    Run your code and report: final solution, and plot the progress of the average
    fitness of the population and the global best particle fitness.
'''


def q_one_three():
    c1 = c2 = 2.05
    w = 0.5

    swarm = [
        Particle(x_y_range, x_y_range) for i in range(100)
    ]
    velocity_position_fn = constriction_velocity(x_y_range, x_y_range, c1, c2)

    avg_fit, best_fit, g_best = simulation(
        termination_condition=termination_condition(iterations),
        swarm=swarm,
        fitness_function=six_hump_camelback,
        velocity_position_update=velocity_position_fn
    )
    test = "Constriction Coefficient PSO"
    title = f"Fitness vs Iterations: {test}"
    data = [("Average Fitness", avg_fit)]
    data.append(("Best Fitness", best_fit))

    graph(title, data)
    print(test)
    print(f"\t c1: {c1}")
    print(f"\t c2: {c2}")
    print(f"\t iterations: {iterations}")
    print(f"\t particles: {particle_count}")
    print(f"\t best fitness: {six_hump_camelback(g_best[0],g_best[1])}")
    print(f"\t best x,y: {g_best[0]} {g_best[1]}")


'''
    Use Constriction Factor version of velocity update equation with Global Best.
    Run your code and report: final solution, and plot the progress of the average
    fitness of the population and the global best particle fitness.
'''


def q_one_four():
    c1 = c2 = 2.05
    w = 0.5

    swarm = [
        Particle(x_y_range, x_y_range) for i in range(100)
    ]
    velocity_position_fn = guaranteed_convergence_velocity(x_y_range, x_y_range, w, c1, c2)

    avg_fit, best_fit, g_best = simulation(
        termination_condition=termination_condition(iterations),
        swarm=swarm,
        fitness_function=six_hump_camelback,
        velocity_position_update=velocity_position_fn
    )
    test = "Guaranteed Convergence PSO"
    title = f"Fitness vs Iterations: {test}"
    data = [("Average Fitness", avg_fit)]
    data.append(("Best Fitness", best_fit))

    graph(title, data)
    print(test)
    print(f"\t c1: {c1}")
    print(f"\t c2: {c2}")
    print(f"\t w: {w}")
    print(f"\t iterations: {iterations}")
    print(f"\t particles: {particle_count}")
    print(f"\t best fitness: {six_hump_camelback(g_best[0],g_best[1])}")
    print(f"\t best x,y: {g_best[0]} {g_best[1]}")

algos = [q_one_one, q_one_two, q_one_three, q_one_four]
# for fn in [q_one_one, q_one_two, q_one_three, q_one_four]:
#     fn()

if len(sys.argv) > 1:
    algos[int(sys.argv[1])]()
else:
    for fn in algos:
        fn()
