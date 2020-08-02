import numpy as np
from individual import Individual
from nodes import *
from six_multiplexer import fitness


def variation(
        p_m=0,
        internal_p=1.0):
    def f(individuals):
        new_pop = []
        if np.random.uniform() < p_m:
            new_pop = mutate_pop(individuals)
        else:
            new_pop = crossover_pop(individuals)
        for i in range(len(new_pop)):
            new_pop[i].fitness = fitness(new_pop[i])
        return new_pop
    return f


def crossover_pop(population):
    new_pop = []
    np.random.shuffle(population)
    for i in range(1, len(population), 2):
        program_a, program_b = crossover_program(
            population[i-1].program, population[i].program)
        new_pop.append(Individual(program=program_a))
        new_pop.append(Individual(program=program_b))
    return new_pop


def crossover_program(program_a_old, program_b_old):
    # Need a deep copy or else there will be loops in the AST
    a = program_a_old.copy()
    b = program_b_old.copy()

    nodes_a = program_to_list(a)
    nodes_b = program_to_list(b)

    parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
    parent_b, rand_node_b = nodes_b[np.random.choice(len(nodes_b))]

    if parent_a is None:
        a = rand_node_b
    else:
        parent_a.children[parent_a.children.index(rand_node_a)] = rand_node_b

    if parent_b is None:
        b = rand_node_a
    else:
        parent_b.children[parent_b.children.index(rand_node_b)] = rand_node_a
    return a, b


def mutate_pop(individuals):
    new_pop = []
    for i in range(len(individuals)):
        program_a = mutate_program(individuals[i].program)
        new_pop.append(Individual(program=program_a))
    return new_pop


def mutate_program(p):
    a = p.copy()
    nodes_a = program_to_list(a)
    parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
    new_node = random_node(
        depth=rand_node_a.depth,
        max_depth=rand_node_a.max_depth,
        full_mode=rand_node_a.full_mode
    )
    if parent_a is None:
        a = new_node
    else:
        # Generate a new sub tree with same depth params
        parent_a.children[parent_a.children.index(rand_node_a)] = new_node
    return a


def program_to_list(program):
    nodes = []
    queue = [(None, program)]
    while len(queue) > 0:
        parent, node = queue.pop()
        nodes.append((parent, node))
        if isinstance(node, Terminal):
            continue
        for child in node.children:
            queue.append((node, child))
    return nodes
