from node_interface import Node
import random
import numpy as np
from six_multiplexer import VARS


class And(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=[None]*2,
                 debug=False):
        super().__init__(
            debug=debug)
        self.children = random_children(
            len(children), depth, max_depth) if depth < max_depth else [Terminal(), Terminal()]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) and self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} AND {self.children[1].to_string()})"


class Or(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=[None]*2,
                 debug=False):
        super().__init__(
            debug=debug)
        self.children = random_children(
            len(children), depth, max_depth) if depth < max_depth else [Terminal(), Terminal()]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) or self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} OR {self.children[1].to_string()})"


class If(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=[None]*3,
                 debug=False):
        super().__init__(debug=debug)
        self.children = random_children(
            len(children), depth, max_depth) if depth < max_depth else [Terminal(), Terminal(), Terminal()]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) if self.children[1].evaluate(inputs) else self.children[2].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} IF {self.children[1].to_string()} ELSE {self.children[2].to_string()})"


class Not(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=[None]*1,
                 debug=False):
        super().__init__(
            debug=debug)
        self.children = random_children(
            len(children), depth, max_depth) if depth < max_depth else [Terminal()]

    def evaluate(self, inputs):
        return not self.children[0].evaluate(inputs)

    def to_string(self):
        return f"(NOT {self.children[0].to_string()})"


class Terminal(Node):
    def __init__(self,
                 depth=None,
                 max_depth=None,
                 children=[np.random.choice(VARS)],
                 debug=False):
        super().__init__(debug=debug)
        self.children = children

    def evaluate(self, inputs):
        return inputs[self.children[0]]

    def to_string(self):
        return f"({self.children[0]})"


T_UNION_F = [And, Or, If, Not, Terminal]


def random_children(i, depth, max_depth):
    return [node(depth+1, max_depth) for node in np.random.choice(T_UNION_F, size=i)]
