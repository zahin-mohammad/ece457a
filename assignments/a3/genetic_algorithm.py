from pid_ga import ProportionalIntegralDifferentialGAS


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
        parents, best_of_current = parent_selection(population)
        children = crossover(parents)
        children = mutation(children)
        population = survivor_selection(children, best_of_current)
        if debug:
            print(f'finished generation: {i+1}', flush=True)
        best_per_generation.append(best_of_generation(population))
    return


if __name__ == "__main__":
    default_PID_GAS = ProportionalIntegralDifferentialGAS()
    simulation(
        default_PID_GAS.generation_count,
        default_PID_GAS.init_population,
        default_PID_GAS.parent_selection,
        default_PID_GAS.crossover,
        default_PID_GAS.mutation,
        default_PID_GAS.survivor_selection,
        default_PID_GAS.best_of_population,
        True
    )
