from six_multiplexer import fitness
import numpy as np
import heapq


def parent_selection(individuals):
    fitnesses = np.array([fitness(individual)
                          for individual in individuals])
    selection_prob = fitnesses / fitnesses.sum()
    # Spin roulette wheel until we get population size number of individuals
    new_gen = [individuals[i] for i in np.random.choice(
        len(individuals), len(individuals), p=selection_prob)]
    return new_gen


def survivor_selection(population_size, survival_count):
    def f(next_generation, current_generation):
        # keep a pop of population_size always
        # remove survivor count number of worst individuals from new pop and
        # replace with survivor count of best individuaLS old pop
        return heapq.nsmallest(
            population_size - survival_count, next_generation, key=lambda x: fitness(x)) + heapq.nlargest(
            survival_count, current_generation, lambda x: fitness(x))
    return f


def best_of_generation(population):
    best_individual = max(population, key=lambda x: fitness(x))
    return fitness(best_individual), best_individual.program.to_string()
