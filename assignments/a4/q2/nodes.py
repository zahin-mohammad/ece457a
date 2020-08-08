import random
import numpy as np
from six_multiplexer import VARS, FUNCTION_NAME
# from elevn_multiplexer import VARS, FUNCTION_NAME
from ete3 import Tree, TreeStyle, TextFace, TreeNode

class Node:
    def __init__(self, children, depth, max_depth, fullmode, function_type):
        self.children, self.depth, self.max_depth, self.full_mode, self.function_type = children, depth, max_depth, fullmode, function_type
    
    # Max from root
    def get_max_depth(self):
        return max(child.get_max_depth() for child in self.children)
    
    # Max from where you call it from
    def get_depth(self):
        return 1 + max(child.get_max_depth() for child in self.children)

    def to_tree_node(self):
        t = Tree(f"{self.function_type};", format=1)
        for child in self.children:
            t.add_child(child.to_tree_node())
        tf = TextFace(f"{self.function_type}")
        tf.rotation = -90
        t.add_face(tf, column=1, position="branch-top")
        return t
    
    def to_diagram(self):
        t = self.to_tree_node()
        ts = TreeStyle()
        ts.show_leaf_name = False
        ts.show_scale = False
        ts.rotation = 90
        t.render(f"./diagrams/{FUNCTION_NAME}_{self.fitness}.png", tree_style=ts)

    def evaluate(self):
        assert False, "Not Implemented"

    def to_string(self):
        assert False, "Not Implemented"

    def copy(self):
        assert False, "Not Implemented"
    
    def to_list(self):
        nodes = [self.copy()]
        for child in self.children:
            nodes.extend(child.to_list())
        return nodes


class And(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 full_mode,
                 children=None,
                 debug=False):
        super().__init__(children, depth, max_depth, full_mode, function_type = And.__name__)

        if self.children is None:
            self.children = random_children(2, depth, max_depth, full_mode)

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) and self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} AND {self.children[1].to_string()})"

    def copy(self):
        return And(
            depth=self.depth,
            max_depth=self.max_depth,
            full_mode=self.full_mode,
            children=[child.copy() for child in self.children])


class Or(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 full_mode,
                 children=None):
        super().__init__(children, depth, max_depth, full_mode, function_type = Or.__name__)

        if self.children is None:
            self.children = random_children(2, depth, max_depth, full_mode)

    def evaluate(self, inputs):
        return self.children[0].evaluate(inputs) or self.children[1].evaluate(inputs)

    def to_string(self):
        return f"({self.children[0].to_string()} OR {self.children[1].to_string()})"

    def copy(self):
        return Or(
            depth=self.depth,
            max_depth=self.max_depth,
            full_mode=self.full_mode,
            children=[child.copy() for child in self.children])


class If(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 full_mode,
                 children=None):
        super().__init__(children, depth, max_depth, full_mode, function_type = If.__name__)

        if self.children is None:
            self.children = random_children(3,depth, max_depth, full_mode) 

    def evaluate(self, inputs):
        return self.children[1].evaluate(inputs) if self.children[0].evaluate(inputs) else self.children[2].evaluate(inputs)

    def to_string(self):
        return f"({self.children[1].to_string()} IF {self.children[0].to_string()} ELSE {self.children[2].to_string()})"

    def to_tree_node(self):
        t = Tree("IF;", format=1)
        t.add_child(self.children[1].to_tree_node())
        t.add_child(self.children[0].to_tree_node())
        t.add_child(self.children[2].to_tree_node())
        tf = TextFace("IF")
        tf.rotation = -90
        t.add_face(tf, column=1, position="branch-top")
        return t

    def copy(self):
        return If(
            depth=self.depth,
            max_depth=self.max_depth,
            full_mode=self.full_mode,
            children=[child.copy() for child in self.children])


class Not(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 full_mode,
                 children=None):
        super().__init__(children, depth, max_depth, full_mode, function_type = Not.__name__)

        if self.children is None:
            self.children = random_children(1, depth, max_depth, full_mode) 

    def evaluate(self, inputs):
        return not self.children[0].evaluate(inputs)

    def to_string(self):
        return f"(NOT {self.children[0].to_string()})"

    def copy(self):
        return Not(
            depth=self.depth,
            max_depth=self.max_depth,
            full_mode=self.full_mode,
            children=[child.copy() for child in self.children])


class Terminal(Node):
    def __init__(self,
                 depth,
                 max_depth,
                 full_mode,
                 children=[None]):
        super().__init__(children, depth, max_depth, full_mode, function_type = Terminal.__name__)

        self.children = [np.random.choice(VARS)]

    def get_max_depth(self):
        return self.depth

    def get_depth(self):
        return 0

    def evaluate(self, inputs):
        return bool(inputs[self.children[0]])

    def to_string(self):
        return f"({self.children[0]})"

    def to_tree_node(self):
        t = Tree(f"{self.children[0]};", format=1)
        tf = TextFace(f"{self.children[0]}")
        tf.rotation = -90
        t.add_face(tf, column=1, position="branch-bottom")
        return t
    
    def to_list(self):
        return [self.copy()]

    def copy(self):
        return Terminal(
            depth=self.depth,
            max_depth=self.max_depth,
            full_mode=self.full_mode,
            children=self.children
        )


T_UNION_F = [And, Or, If, Not, Terminal]
F = [And, Or, If, Not]

def random_children(child_count, depth, max_depth, full_mode):
    if depth >= max_depth:
        return [Terminal(depth+1, max_depth, full_mode) for i in range(child_count)]
    function_set = F if full_mode else T_UNION_F
    return [node(depth+1, max_depth, full_mode) for node in np.random.choice(function_set, size=child_count)]


def random_node(depth, max_depth, full_mode):
    function_set = F if full_mode else T_UNION_F
    return (np.random.choice(function_set))(
        depth=depth,
        max_depth=max_depth,
        full_mode= not full_mode)
