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

            def dfs(n, depth):
                if isinstance(n, Terminal):
                    return depth + 1
                return max([
                    dfs(c, depth+1) for c in n.children
                ])
            print(
                f'\tMax Pop Depth: {max([dfs(i.program, 0) for i in population])}')

        if best_per_generation[-1] == 1.0:
            break
    if debug:
        print(f"Simulation finished in : {time.time() - sim_start}")
    return best_per_generation
