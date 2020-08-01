
class Node:
    def __init__(self,
                 num_params=0,
                 debug=False):
        self.children = []
        self.debug = debug
        self.num_params = num_params
        pass

    def evaluate(self):
        pass

    def to_string(self):
        print("TODO")
