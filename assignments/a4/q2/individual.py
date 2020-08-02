from nodes import *
import numpy as np


class Individual:
    def __init__(self, max_depth=3):
        self.program = (np.random.choice(T_UNION_F))(0, max_depth)
        self.fitness = None

    def program_to_list(self):
        nodes = []
        queue = [(None, self.program)]
        while len(queue) > 0:
            parent, node = queue.pop()
            nodes.append((parent, node))
            if isinstance(node, Terminal):
                continue
            for child in node.children:
                queue.append((node, child))
        return nodes


if __name__ == "__main__":
    individual = Individual()
    nodes = individual.program_to_list()
    for node in nodes:
        print(node[1].to_string())
