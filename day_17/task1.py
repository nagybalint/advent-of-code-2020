from collections import defaultdict
import os
from typing import Dict

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6

# e.g grid[z][x][y] = ACTIVE 
grid = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: INACTIVE
        )
    )
)

def parse_input(file_name: str):
    with open(file_name) as f:
        for i, row in enumerate(f.readlines()):
            for j, cube in enumerate(list(row.strip())):
                grid[0][i][j] = cube

def toggle_cube(x: int, y: int, z: int):
    if grid[z][x][y] == ACTIVE:
        grid[z][x][y] = INACTIVE
    else:
        grid[z][x][y] = ACTIVE

def count_active_neighbors(x: int, y: int, z: int):
    num_of_actives = 0

    for i in neighbors_for(x):
        for j in neighbors_for(y):
            for k in neighbors_for(z):
                if i == x and j == y and k == z:
                    continue
                else:
                    if grid[k][i][j] == ACTIVE:
                        num_of_actives += 1
    
    return num_of_actives

def neighbors_for(n: int):
    return [n-1, n, n+1]

def get_grid_range(coord):
    return list(range(min(coord) - 1, max(coord) + 2))

def iterate_grid():
    xs = set()
    ys = set()
    zs = set()
    for z, layer in grid.items():
        zs.add(z)
        for x, row in layer.items():
            xs.add(x)
            for y, _ in row.items():
                ys.add(y)

    elements = []
    for z in get_grid_range(zs):
        for x in get_grid_range(xs):
            for y in get_grid_range(ys):
                 elements.append((x,y,z, grid[z][x][y]))
    return elements

def calculate_answer() -> int:
    for _ in range(CYCLES):
        toggle_list = []
        for x, y, z, cube in iterate_grid():
            active_neighbors = count_active_neighbors(x,y,z)
            if cube == ACTIVE and not 2 <= active_neighbors <= 3:
                toggle_list.append((x,y,z))
            if cube == INACTIVE and active_neighbors == 3:
                toggle_list.append((x,y,z))
        for x,y,z in toggle_list:
            toggle_cube(x,y,z)
    active_cubes = 0
    for x, y, z, cube in iterate_grid():
        if cube == ACTIVE:
            active_cubes += 1
    return active_cubes

def get_grid_layer(z):
    layer = []
    xs = list(grid[z].keys())
    xs.sort()
    for x in xs:
        layer.append([])
        ys = list(grid[z][x].keys())
        ys.sort()
        for y in ys:
            layer[-1].append(grid[z][x][y])
    return layer

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    parse_input(file_path)
    answer = calculate_answer()
    print(answer)