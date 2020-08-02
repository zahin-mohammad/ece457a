from genetic_programming import simulation
from individual import Individual
from six_multiplexer import fitness
import heapq
import numpy as np
from nodes import *


def init_population(num_individuals):
    def f():
        return [Individual() for i in range(num_individuals)]
    return f


def parent_selection(individuals):
    fitnesses = np.array([fitness(individual)
                          for individual in individuals])
    selection_prob = fitnesses / fitnesses.sum()
    # Spin roulette wheel until we get population size number of individuals
    new_gen = [individuals[i] for i in np.random.choice(
        len(individuals), len(individuals), p=selection_prob)]
    return new_gen


def variation(
        p_m=0.05,
        internal_p=1.0):
    def f(individuals):
        if np.random.uniform() <= p_m:
            pass
        else:
            crossover_pop(individuals)
    return f


def crossover_pop(population):
    np.random.shuffle(population)
    for i in range(1, len(population), 2):
        crossover_individual(population[i-1], population[i])


def crossover_individual(individual_a, individual_b):
    # in place crossover
    nodes_a = individual_a.program_to_list()
    nodes_b = individual_b.program_to_list()

    parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
    parent_b, rand_node_b = nodes_b[np.random.choice(len(nodes_b))]

    if parent_a is None:
        individual_a = rand_node_b
    else:
        parent_a.children[parent_a.children.index(rand_node_a)] = rand_node_b

    if parent_b is None:
        individual_b = rand_node_a
    else:
        parent_b.children[parent_b.children.index(rand_node_b)] = rand_node_a


def mutation(individuals):
    pass


def survivor_selection(population_size, survival_count):
    def f(next_generation, current_generation):
        # keep a pop of population_size always
        # remove survivor count number of worst individuals from new pop and
        # replace with survivor count of best individuaLS old pop
        return heapq.nsmallest(
            population_size - survival_count, next_generation, key=lambda x: x.fitness) + heapq.nlargest(
            survival_count, current_generation, lambda x: x.fitness)
    return f


def best_of_generation(population):
    best_individual = max(population, key=lambda x: x.fitness)
    return best_individual.fitness, best_individual.program.to_string()


# a, b = Individual(), Individual()
# print(a.program.to_string())
# print(b.program.to_string())
# crossover_individual(a, b)
# print(a.program.to_string())
# print(b.program.to_string())

num_individuals = 10
generation_count = 10
survivor_count = 2
simulation(
    generation_count=generation_count,
    init_population=init_population(num_individuals),
    parent_selection=parent_selection,
    variation=variation(),
    survivor_selection=survivor_selection(num_individuals, survivor_count),
    best_of_generation=best_of_generation,
    debug=True
)
