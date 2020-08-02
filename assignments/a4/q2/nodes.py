from node_interface import Node
import random
import numpy as np
from six_multiplexer import VARS


class And(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=None,
                 debug=False):
        super().__init__(children, depth, max_depth)

        if self.children is None:
            self.children = random_children(
                2, depth, max_depth) if depth < max_depth else [Terminal(depth+1, max_depth) for i in range(2)]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) and self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} AND {self.children[1].to_string()})"

    def copy(self):
        return And(
            depth=self.depth,
            max_depth=self.max_depth,
            children=[child.copy() for child in self.children])


class Or(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=None,
                 debug=False):
        super().__init__(children, depth, max_depth)

        if self.children is None:
            self.children = random_children(
                2, depth, max_depth) if depth < max_depth else [Terminal(depth+1, max_depth) for i in range(2)]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) or self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} OR {self.children[1].to_string()})"

    def copy(self):
        return Or(
            depth=self.depth,
            max_depth=self.max_depth,
            children=[child.copy() for child in self.children])


class If(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=None,
                 debug=False):
        super().__init__(children, depth, max_depth)

        if self.children is None:
            self.children = random_children(
                3, depth, max_depth) if depth < max_depth else [Terminal(depth+1, max_depth) for i in range(3)]

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) if self.children[1].evaluate(inputs) else self.children[2].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} IF {self.children[1].to_string()} ELSE {self.children[2].to_string()})"

    def copy(self):
        return If(
            depth=self.depth,
            max_depth=self.max_depth,
            children=[child.copy() for child in self.children])


class Not(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=None,
                 debug=False):
        super().__init__(children, depth, max_depth)

        if self.children is None:
            self.children = random_children(
                1, depth, max_depth) if depth < max_depth else [Terminal(depth+1, max_depth)]

    def evaluate(self, inputs):
        return not self.children[0].evaluate(inputs)

    def to_string(self):
        return f"(NOT {self.children[0].to_string()})"

    def copy(self):
        return Not(
            depth=self.depth,
            max_depth=self.max_depth,
            children=[child.copy() for child in self.children])


class Terminal(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 children=[None],
                 debug=False):
        super().__init__(children, depth, max_depth)

        self.children = [np.random.choice(VARS)]

    def evaluate(self, inputs):
        return inputs[self.children[0]]

    def to_string(self):
        return f"({self.children[0]})"

    def copy(self):
        return Terminal(
            depth=self.depth,
            max_depth=self.max_depth,
            children=self.children
        )  # Don't need to regen Terminal Nodes because they don't add depth


T_UNION_F = [And, Or, If, Not, Terminal]


def random_children(i, depth, max_depth):
    return [node(depth+1, max_depth) for node in np.random.choice(T_UNION_F, size=i)]
