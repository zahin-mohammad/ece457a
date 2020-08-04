import numpy as np
from individual import Individual
from nodes import *
from six_multiplexer import fitness


def variation(p_m=0):
    def f(parents):
        # Don't modify parents
        individuals = [parent.copy() for parent in parents]
        np.random.shuffle(individuals)
        intermediate_pool = []

        while len(intermediate_pool) < len(individuals):
            i = len(intermediate_pool)
            if np.random.uniform() < p_m:
                p = mutate_program(
                    individuals[i].program.copy())
                intermediate_pool.append(Individual(
                    program=p.copy(),
                    max_depth=individuals[i].max_depth))
            else:
                # Wrap around if at end
                a_index = i
                b_index = i+1 if i != len(individuals)-1 else 0

                p_a, p_b = crossover_program(
                    individuals[a_index].program.copy(),
                    individuals[b_index].program.copy())

                intermediate_pool.append(Individual(
                    program=p_a.copy(),
                    max_depth=individuals[a_index].max_depth))
                intermediate_pool.append(Individual(
                    program=p_b.copy(),
                    max_depth=individuals[b_index].max_depth))
        return intermediate_pool
    return f


def crossover_program(a, b):
    temp1 = a.to_string()
    nodes_a, nodes_b = program_to_list(a), program_to_list(b)
    np.random.shuffle(nodes_a)
    np.random.shuffle(nodes_b)

    # replace rand_node_x (child) from parent_x
    # Each node equally likely to get swapped
    
    parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
    parent_b, rand_node_b = nodes_b[np.random.choice(len(nodes_b))]
    while True:
        # Do not want to replace root
        depth_a = rand_node_a.get_max_depth()
        depth_b = rand_node_b.get_max_depth()
        if (parent_a == None and depth_a != 0 ) \
            or (parent_b == None and depth_b != 0) \
            or (depth_a!= depth_b):
            parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
            parent_b, rand_node_b = nodes_b[np.random.choice(len(nodes_b))]
        else:
            break
    if parent_a:
        parent_a.children[parent_a.children.index(rand_node_a)] = rand_node_b
    else:
        a = rand_node_b

    if parent_b:
        parent_b.children[parent_b.children.index(rand_node_b)] = rand_node_a
    else:
        b = rand_node_a

    temp2 = a.to_string()
    return a, b


def mutate_program(a):
    nodes_a = program_to_list(a)
    np.random.shuffle(nodes_a)

    parent_a, rand_node_a = nodes_a[np.random.choice(len(nodes_a))]
    # Generate a new sub tree with same depth params
    new_node = random_node(
        depth=rand_node_a.depth,
        max_depth=rand_node_a.max_depth,
        full_mode=rand_node_a.full_mode
    )
    if parent_a:
        parent_a.children[parent_a.children.index(rand_node_a)] = new_node
    else:
        a = new_node
    return a

# BFS to generate all lists of <parent, child>
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


if __name__ == "__main__":
    variation_fn = variation()

    p = [Individual(3) for i in range(10)]
    n_p = variation_fn(variation_fn(variation_fn(p)))
