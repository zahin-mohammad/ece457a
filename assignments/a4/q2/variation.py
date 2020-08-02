import numpy as np
from individual import Individual
from nodes import *
from six_multiplexer import fitness


def variation(
        p_m=0):
    def f(individuals):
        # Don't modify population
        population = [individual.copy() for individual in individuals]

        if np.random.uniform() < p_m:
            population = mutate_pop(population)
        else:
            population = crossover_pop(population)

        # Update Fitness
        for i in range(len(population)):
            population[i].fitness = fitness(population[i].program)
        return population
    return f


def crossover_pop(population):
    np.random.shuffle(population)
    for i in range(1, len(population), 2):
        population[i-1].program, population[i].program = crossover_program(
            population[i-1].program, population[i].program)
    return population


def mutate_pop(population):
    for i in range(len(population)):
        population[i].program = mutate_program(population[i].program)
    return population


def crossover_program(a, b):
    nodes_a, nodes_b = program_to_list(a), program_to_list(b)
    np.random.shuffle(nodes_a)
    np.random.shuffle(nodes_b)

    # replace rand_node_x (child) from parent_x
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


def mutate_program(a):
    nodes_a = program_to_list(a)
    np.random.shuffle(nodes_a)

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


def program_to_list(root_node):
    nodes = []
    queue = [(None, root_node)]

    while len(queue) > 0:
        parent, node = queue.pop()
        nodes.append((parent, node))
        if isinstance(node, Terminal):
            continue
        for child in node.children:
            queue.append((node, child))
    return nodes

# def node_collector(nodes, node: ProgramTreeNode, parent: ProgramTreeNode = None):
#     nodes.append((node, parent))

#     for child in node.children:
#         node_collector(nodes, child, node)
