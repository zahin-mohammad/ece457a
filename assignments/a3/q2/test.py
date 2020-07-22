from coord import coordinates
from typing import Callable, Tuple
import math

def get_distance(coord:Tuple[int,int]) -> float:
        i,j = coord
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# path = [5, 13, 2, 20, 26, 14, 17, 16, 21, 9, 22, 6, 1, 12, 18, 11, 0, 24, 10, 15, 4, 28, 7, 23, 27, 8, 25, 19, 3, 5]
path = [7, 26, 15, 23, 0, 27, 5, 11, 8, 4, 25, 28, 2, 1, 20, 12, 9, 19, 3, 14, 17, 13, 16, 21, 10, 18, 24, 6, 22, 7]
distance = 0
for i in range(1, len(path)):
    distance += get_distance((path[i-1], path[i]))
print(distance)