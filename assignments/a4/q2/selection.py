from six_multiplexer import fitness
import numpy as np
import heapq


def parent_selection(x=0.5):
    def f(population):
        # TODO: Change this once it works
        x_count = min(int(np.round(x * len(population))), len(population))

        population = sorted(
            population, key=lambda program: program.fitness, reverse=True)

        group1 = population[:x_count]
        group2 = population[x_count:]

        group1_total_fitness = sum([program.fitness for program in group1])
        group2_total_fitness = sum([program.fitness for program in group2])

        group1_pick_probs = [program.fitness /
                             group1_total_fitness for program in group1]

        group2_pick_probs = [program.fitness /
                             group2_total_fitness for program in group2]

        parents = []

        # 80% from best x% of population
        # 20% from best (100-x)% of population
        for _ in range(len(population)):
            group, pick_probs = [(group1, group1_pick_probs), (group2,
                                                               group2_pick_probs)][np.random.choice([0, 1], p=[0.8, 0.2])]

            parents.append((np.random.choice(group, p=pick_probs)).copy())

        return parents
    return f


def survivor_selection(population_size, survival_count):
    def f(next_generation, current_generation):
        # keep a pop of population_size always
        # remove survivor count number of worst individuals from new pop and
        # replace with survivor count of best individuaLS old pop
        return heapq.nlargest(
            population_size - survival_count, next_generation, key=lambda x: x.fitness) + heapq.nlargest(
            survival_count, current_generation, lambda x: x.fitness)
    return f


def best_of_generation(population):
    return (max(population, key=lambda x: x.fitness)).fitness
