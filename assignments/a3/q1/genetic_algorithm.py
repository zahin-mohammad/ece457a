from pid_ga import ProportionalIntegralDifferentialGAS
import time
import sys
import matplotlib.pyplot as plt


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
        best_fitness, best_individual = best_of_generation(population)
        best_per_generation.append(best_fitness)
        end = time.time()
        if debug:
            print(
                f'For gen: {i+1} fitness:{best_per_generation[-1]} took: {end-start} s', flush=True)
            print(f'\tbest_individual:{best_individual}', flush=True)
            print(f'\tpop-size: {len(population)}')

    return best_per_generation


if __name__ == "__main__":

    def get_fitness(pid):
        return simulation(
            pid.generation_count,
            pid.init_population,
            pid.parent_selection,
            pid.crossover,
            pid.mutation,
            pid.survivor_selection,
            pid.best_of_population,
            True
        )

    def graph(title, data):
        for series in data:
            has_legend = False
            x = range(1, len(series[1])+1)
            y = series[1]
            if series[0] == '':
                plt.plot(x, y)
            else:
                has_legend = True
                plt.plot(x, y, label=series[0])

        plt.xlabel('Generations')
        plt.ylabel('Fitness')
        if has_legend:
            plt.legend()
        plt.title(title)

        plt.savefig(title, dpi=500)

    pid = ProportionalIntegralDifferentialGAS()
    if sys.argv[1] == '0':
        title = "Fitness vs Generation Count"
        data = []
        for i in range(3):
            generation_count = (i+1)*50
            pid.reset(generation_count=generation_count)
            data.append(
                (f'generation-count: {generation_count}', get_fitness(pid)))
        graph(title, data)

    elif sys.argv[1] == '1':
        title = "Fitness vs Population Size"
        data = []
        for i in range(3):
            population_size = (i+1)*25
            pid.reset(population_size=population_size)
            data.append(
                (f'pop-size: {population_size}', get_fitness(pid)))
        graph(title, data)

    elif sys.argv[1] == '2':
        title = "Fitness vs Crossover Probability"
        data = []
        for i in range(3):
            # 0.6 -> 0.9
            prob_crossover = 0.6+(i)*0.1
            pid.reset(prob_crossover=prob_crossover)
            data.append(
                (f'p_c: {prob_crossover}', get_fitness(pid)))
        graph(title, data)

    elif sys.argv[1] == '3':
        title = "Fitness vs Mutation Probability"
        data = []
        for i in range(3):
            # 0.3 -> 0.6
            prob_mutation = 0.3 + (i)*0.1
            pid.reset(prob_mutation=prob_mutation)
            data.append(
                (f'p_m: {prob_mutation}', get_fitness(pid)))
        graph(title, data)

    elif sys.argv[1] == '4':
        title = "Fitness vs Generation"
        data = []
        pid = ProportionalIntegralDifferentialGAS()
        data.append((f'', get_fitness(pid)))
        graph(title, data)
