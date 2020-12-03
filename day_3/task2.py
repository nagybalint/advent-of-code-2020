import math
import os
from task1 import map_to_grid, count_trees

OPEN_SPOT = '.'
TREE = '#'  

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    grid = map_to_grid(file_path)
    answers = [count_trees(grid, 0, 0, slope[1], slope[0]) for slope in [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]]
    answer = math.prod(answers)
    print(f'Encountered {answer} trees')