import os
from typing import List

OPEN_SPOT = '.'
TREE = '#'

def map_to_grid(filepath: str) -> List[List[str]]:
    with open(filepath) as f:
        return [list(line.strip()) for line in f.readlines()]
    
def count_trees(grid: List[List[str]], r: int, c: int, slope_r: int, slope_c: int) -> int:
    height = len(grid)
    width = len(grid[0])
    if r < height:
        current_pos = grid[r][c%width]
        if current_pos == TREE:
            return 1 + count_trees(grid, r + slope_r, c + slope_c, slope_r, slope_c)
        return count_trees(grid, r + slope_r, c + slope_c, slope_r, slope_c)
    return 0
    

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    grid = map_to_grid(file_path)
    answer = count_trees(grid, 0, 0, 1, 3)
    print(f'Encountered {answer} trees')
    
    