from collections import defaultdict
import os
from typing import Dict

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6

# e.g grid[z][w][x][y] = ACTIVE 
grid = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(
                lambda: INACTIVE
            )
        )
    )
)

def parse_input(file_name: str):
    with open(file_name) as f:
        for i, row in enumerate(f.readlines()):
            for j, cube in enumerate(list(row.strip())):
                grid[0][0][i][j] = cube

def toggle_cube(x: int, y: int, z: int, w: int):
    if grid[z][w][x][y] == ACTIVE:
        grid[z][w][x][y] = INACTIVE
    else:
        grid[z][w][x][y] = ACTIVE

def count_active_neighbors(x: int, y: int, z: int, w: int):
    num_of_actives = 0

    for i in neighbors_for(x):
        for j in neighbors_for(y):
            for k in neighbors_for(z):
                for l in neighbors_for(w):
                    if i == x and j == y and k == z and l == w:
                        continue
                    else:
                        if grid[k][l][i][j] == ACTIVE:
                            num_of_actives += 1
    
    return num_of_actives

def neighbors_for(n: int):
    return [n-1, n, n+1]

def get_grid_limits():
    def get_coord_range(c):
        return list(range(min(c) - 1, max(c) + 2))

    xs = set()
    ys = set()
    zs = set()
    ws = set()
    for z, cube in grid.items():
        zs.add(z)
        for w, layer in cube.items():
            ws.add(w)
            for x, row in layer.items():
                xs.add(x)
                for y, _ in row.items():
                    ys.add(y)

    return get_coord_range(xs), get_coord_range(ys), get_coord_range(zs), get_coord_range(ws)

def iterate_grid():
    x_range, y_range, z_range, w_range = get_grid_limits()
    for z in z_range:
        for w in w_range:
            for x in x_range:
                for y in y_range:
                    yield x, y, z, w, grid[z][w][x][y]

def calculate_answer() -> int:
    for _ in range(CYCLES):
        execute_cycle()
    return count_active_cubes()

def count_active_cubes():
    active_cubes = 0
    for _, cube in grid.items():
        for _, layer in cube.items():
            for _, row in layer.items():
                for _, val in row.items():
                    if val == ACTIVE:
                        active_cubes += 1
    return active_cubes

def execute_cycle():
    toggle_list = []
    for x, y, z, w, cube in iterate_grid():
        active_neighbors = count_active_neighbors(x,y,z,w)
        if cube == ACTIVE and not 2 <= active_neighbors <= 3:
            toggle_list.append((x,y,z,w))
        if cube == INACTIVE and active_neighbors == 3:
            toggle_list.append((x,y,z,w))
    for x,y,z,w in toggle_list:
        toggle_cube(x,y,z,w)

def print_grid_layer(z, w):
    x_range, y_range, _, _ = get_grid_limits()
    return [[grid[z][w][x][y] for y in y_range] for x in x_range]

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    parse_input(file_path)
    answer = calculate_answer()
    print(answer)