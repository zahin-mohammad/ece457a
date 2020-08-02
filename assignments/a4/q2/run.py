from genetic_programming import simulation
from selection import *
from individual import Individual
from variation import variation
import numpy as np


def init_population(num_individuals):
    def f():
        return [Individual() for i in range(num_individuals)]
    return f


num_individuals = 1000
generation_count = 1000
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
