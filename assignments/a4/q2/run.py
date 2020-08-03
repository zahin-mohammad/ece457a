import numpy as np
SEED = np.random.randint(1000)
np.random.seed(SEED)
print(f"np SEED: {SEED}")
from ete3 import TreeStyle
import time
from six_multiplexer import fitness
from variation import variation
from individual import Individual
from selection import *
from genetic_programming import simulation



num_individuals = 1000
max_depth = 3
generation_count = 1000
survivor_count = 50
p_m = 0.05
x = 0.5


def init_population(num_individuals, max_depth):
    def f():
        return [Individual(max_depth=1 + (i % max_depth))
                for i in range(num_individuals)]
    return f


best_pre_gen, best_individual = simulation(
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

t = best_individual.program.to_tree_node()
ts = TreeStyle()
ts.show_leaf_name = False
ts.show_scale = False
ts.rotation = 90
t.render(f"example{best_individual.fitness}.png", tree_style=ts)
