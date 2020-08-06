
import numpy as np


def simulation(
    termination_condition,
    swarm,
    fitness_function,
    velocity_position_update,
):
    avg_fitness = []
    best_fitness = []
    g_best = swarm[0].position  # init

    num_failures = 0
    num_success = 0

    for _ in termination_condition():
        v_p_update = velocity_position_update(
            num_failures, num_success, g_best)
        for particle in swarm:
            # update velocity, update position, update personal_best
            particle.fly(
                velocity_position_update_fn=v_p_update,
                fitness_fn=fitness_function)

            new_g_best = min(g_best, particle.position,
                             key=lambda pos: fitness_function(pos[0], pos[1]))

            if tuple(g_best) == tuple(new_g_best):
                num_failures += 1
                num_success = 0
            else:
                num_success += 1
                num_failures = 0
            g_best = new_g_best

        # Simulation data
        avg_fitness.append(np.average(
            np.array([fitness_function(p.position[0], p.position[1])
                      for p in swarm])
        ))

        best_fitness.append(fitness_function(
            g_best[0], g_best[1]))
        # print(
        #     f"Best is {best_fitness[-1]}\tWith x,y: {g_best[0]}\t{g_best[1]}")

    return avg_fitness, best_fitness, g_best
