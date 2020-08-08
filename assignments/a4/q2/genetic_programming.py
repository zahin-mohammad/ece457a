import time
from nodes import Terminal


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

    population, best_per_generation, best_individual = init_population(), [], None
    if debug:
        print(f"Init took: {time.time() - sim_start} s")
    for i in range(generation_count):
        start = time.time()

        population = survivor_selection(
            variation(parent_selection(population)), population)
        best_individual = best_of_generation(population)
        best_per_generation.append(best_individual.fitness)

        if debug:
            print(f'Gen: {i+1}/{generation_count}')
            print(f'\tFitness:{best_per_generation[-1]}')
            print(f'\tTook: {time.time() - start} s')
            print(f'\tPop-size: {len(population)}')
            max_depth_p = max(population, key= lambda x: x.program.get_max_depth())
            print(
                f'\tMax Pop Depth: {max_depth_p.program.get_max_depth()}')
            # if max_depth_p.program.get_max_depth() > 3:
            #     max_depth_p.to_diagram()            

        if best_per_generation[-1] == 1.0:
            break
    if debug:
        print(f"Simulation finished in : {time.time() - sim_start}")
    return best_per_generation, best_individual
