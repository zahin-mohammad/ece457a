
from coord import coordinates
import math
from typing import Callable, Tuple
import numpy as np


class Ant():
    def __init__(self):
        super().__init__()
        self.tabu = set()
        self.solution_path = [np.random.choice(len(coordinates))]
        self.tabu.add(self.solution_path[-1])
        self.solution_length = 0

    def get_distance(self, coord:Tuple[int,int]) -> float:
        i,j = coord
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def add_node(self, new_node: Tuple[int, int]):
        new_node = new_node[0] if new_node[0] not in self.tabu else new_node[1]
        assert new_node not in self.tabu
        self.tabu.add(new_node)
        self.solution_path.append(new_node)
        self.solution_length += self.get_distance((self.solution_path[-2], self.solution_path[-1]))
    
    def loop_back(self):
        self.solution_path.append(self.solution_path[0])
        self.solution_length += self.get_distance((self.solution_path[-2], self.solution_path[-1]))

    def ant_has_solution(self) -> bool:
        return len(self.solution_path) == len(coordinates)

    def get_neighbors(self):
        return [i for i in range(len(coordinates)) if i not in self.tabu]
