from pid_ga import ProportionalIntegralDifferentialGAS
import time
import sys


def simulation(
    generation_count,
    init_population,
    parent_selection,
    crossover,
    mutation,
    survivor_selection,
    best_of_generation,
    debug=False
):
    population = init_population()
    best_per_generation = []
    for i in range(generation_count):
        start = time.time()
        parents = parent_selection(population)
        children = mutation(crossover(parents))
        population = survivor_selection(children, population)
        best_per_generation.append(best_of_generation(population))
        end = time.time()
        if debug:
            print(
                f'For gen: {i+1} fitness:{best_per_generation[-1][0]} for individual: {best_per_generation[-1][1]} took: {end-start}', flush=True)

    return best_per_generation


if __name__ == "__main__":
    default_PID_GAS = ProportionalIntegralDifferentialGAS()
    fitness_per_generation = simulation(
        default_PID_GAS.generation_count,
        default_PID_GAS.init_population,
        default_PID_GAS.parent_selection,
        default_PID_GAS.crossover,
        default_PID_GAS.mutation,
        default_PID_GAS.survivor_selection,
        default_PID_GAS.best_of_population,
        True
    )
    print(fitness_per_generation[-1][0])
    print(fitness_per_generation[-1][1])

    # for i in range(3):
    #     generation_count = (i+1)*50
    #     pid = ProportionalIntegralDifferentialGAS(
    #         generation_count=generation_count)
    # for i in range(3):
    #     population_size = (i+1)*25
    #     pid = ProportionalIntegralDifferentialGAS(
    #         population_size=population_size)
    # for i in range(3):
    #     prob_crossover = (i+1)*0.3
    #     pid = ProportionalIntegralDifferentialGAS(
    #         prob_crossover=prob_crossover)
    # for i in range(3):
    #     prob_mutation = (i+1)*0.125
    #     pid = ProportionalIntegralDifferentialGAS(
    #         prob_mutation=prob_mutation)
