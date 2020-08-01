import time
import sys
import matplotlib.pyplot as plt


def simulation(
    generation_count,
    init_population,
    parent_selection,
    mutation_or_crossover,
    survivor_selection,
    best_of_generation,
    debug=False
):
    population = init_population()
    best_per_generation = []
    for i in range(generation_count):
        start = time.time()
        parents = parent_selection(population)
        children = mutation_or_crossover(parents)
        population = survivor_selection(children, population)
        best_fitness, best_individual = best_of_generation(population)
        best_per_generation.append(best_fitness)
        end = time.time()
        if debug:
            print(
                f'For gen: {i+1} fitness:{best_per_generation[-1]} took: {end-start} s', flush=True)
            print(f'\tbest_individual:{best_individual}', flush=True)
            print(f'\tpop-size: {len(population)}')

    return best_per_generation
