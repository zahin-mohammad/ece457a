
class Node:
    def __init__(self, children, depth, max_depth, fullmode):
        self.children, self.depth, self.max_depth, self.full_mode = children, depth, max_depth, fullmode

    def evaluate(self):
        assert False, "Not Implemented"

    def to_string(self):
        assert False, "Not Implemented"

    def copy(self):
        assert False, "Not Implemented"
