import time


def simulation(
    generation_count,
    init_population,
    parent_selection,
    variation,
    survivor_selection,
    best_of_generation,
    debug=False
):
    sim_start = time.time()

    population, best_per_generation = init_population(), []
    if debug:
        print(f"Init took: {time.time() - sim_start} s")
    for i in range(generation_count):
        start = time.time()

        population = survivor_selection(
            variation(parent_selection(population)), population)
        best_fitness, _ = best_of_generation(population)
        best_per_generation.append(best_fitness)

        if debug:
            print(f'Gen: {i+1}/{generation_count}')
            print(f'\tFitness:{best_fitness}')
            print(f'\tTook: {time.time() - start} s')
            print(f'\tPop-size: {len(population)}')
        if best_fitness == 1.0:
            break
    if debug:
        print(f"Simulation finished in : {time.time() - sim_start}")
    return best_per_generation
