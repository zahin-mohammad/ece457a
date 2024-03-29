import numpy as np
# SEED = np.random.randint(1000)
SEED = 1
np.random.seed(SEED)
print(f"np SEED: {SEED}")
import time
from variation import variation
from individual import Individual
from selection import *
from genetic_programming import simulation
from plot import graph


num_individuals = 1024
max_depth = 2
generation_count = 1024*2
survivor_count = 50
p_m = 0.00
k = 7


def init_population(num_individuals, max_depth):
    def f():
        return [Individual(max_depth=1 + (i % max_depth))
                for i in range(num_individuals)]
    return f


best_per_gen, best_individual = simulation(
    generation_count=generation_count,
    init_population=init_population(
        num_individuals=num_individuals,
        max_depth=max_depth),
    parent_selection=parent_selection(
        k=k
    ),
    variation=variation(
        p_m=p_m),
    survivor_selection=survivor_selection(
        population_size=num_individuals,
        survival_count=survivor_count),
    best_of_generation=best_of_generation,
    debug=True
)

best_individual.to_diagram()
graph(title = "Best Fitness vs  Generation eleven multiplexer", data = [("Eleven Multiplexer", best_per_gen)])
