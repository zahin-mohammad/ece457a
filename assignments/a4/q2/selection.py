import numpy as np
import heapq


def parent_selection(k):
    def f(p):
        pop_size = len(p)
        
        parents = []
        pop_size = len(p)
        population = [i.copy() for i in p if i.fitness != 0]

        while len(parents) < pop_size:
            rand_individuals = list(np.random.choice(population, size=k))
            parents.append(max(rand_individuals, key= lambda x: x.fitness))
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
    return (max(population, key=lambda x: x.fitness))
