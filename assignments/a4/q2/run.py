from genetic_programming import simulation
from selection import *
from individual import Individual
from variation import variation
import numpy as np
from six_multiplexer import fitness
import time

num_individuals = 1000
max_depth = 3
generation_count = 10000
survivor_count = 50
p_m = 0.05
x = 0.5


def init_population(num_individuals, max_depth):
    def f():
        return [Individual(max_depth=1 + (i % max_depth))
                for i in range(num_individuals)]
    return f


simulation(
    generation_count=generation_count,
    init_population=init_population(
        num_individuals=num_individuals,
        max_depth=max_depth),
    parent_selection=parent_selection(
        x=x
    ),
    variation=variation(
        p_m=p_m),
    survivor_selection=survivor_selection(
        population_size=num_individuals,
        survival_count=survivor_count),
    best_of_generation=best_of_generation,
    debug=True
)
