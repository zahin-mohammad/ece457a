
import numpy as np


def simulation(
    termination_condition,
    particles,
    fitness_function,
    velocity_update,
):
    avg_fitness = []
    best_fitness = []
    g_best = particles[0].position  # init

    for i in termination_condition():
        for particle in particles:
            # update velocity, update position, update personal_best
            particle.fly(
                global_best=g_best,
                velocity_update_fn=velocity_update,
                fitness_fn=fitness_function)

            g_best = min(g_best, particle.position,
                         key=lambda pos: fitness_function(pos[0], pos[1]))

        # Simulation data
        avg_fitness.append(np.average(
            np.array([fitness_function(p.position[0], p.position[1])
                      for p in particles])
        ))

        best_fitness.append(fitness_function(
            g_best[0], g_best[1]))
        print(
            f"Best is {best_fitness[-1]}\tWith x,y: {g_best[0]}\t{g_best[1]}")

    return avg_fitness, best_fitness
