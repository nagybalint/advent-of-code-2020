import math
import os
from itertools import chain, groupby
from typing import Dict, List, Tuple

class Tile:
    def __init__(self, str_repr: str):
        self.id = self.__parse_id(str_repr[0])
        self.pixels = str_repr[1:]
        self.borders = self.__parse_borders(self.pixels)

    def __parse_id(self, title: str):
        return int(title[5:-1])

    def __parse_borders(self, pixels: List[List[str]]):
        borders = []
        borders.append(pixels[0])
        borders.append(pixels[-1])
        borders.append(''.join([p[0] for p in pixels]))
        borders.append(''.join([p[-1] for p in pixels]))
        return borders

    def matches(self, other) -> bool:
        for b in self.borders:
            for b_ in other.borders:
                if b == b_ or b == b_[::-1]:
                    return True
        return False

def parse_input(file_name: str) -> Dict[int, Dict]:
    with open(file_name) as f:
        tiles_strings = [list(group) for k, group in groupby([line.strip() for line in f.readlines()], lambda x: x == "") if not k]
        tiles = {}
        for tile in [Tile(tile_string) for tile_string in tiles_strings]:
            tiles[tile.id] = {
                "tile": tile,
                "pairs": []
            }
        return tiles

def calculate_answer(tiles: Dict[int, Dict]) -> int:
    for tile_id_1 in tiles.keys():
        for tile_id_2 in tiles.keys():
            if tile_id_1 == tile_id_2 or tile_id_1 in tiles[tile_id_2]['pairs']:
                continue
            else:
                if tiles[tile_id_1]['tile'].matches(tiles[tile_id_2]['tile']):
                    tiles[tile_id_1]['pairs'].append(tile_id_2)
                    tiles[tile_id_2]['pairs'].append(tile_id_1)
    
    corners = []
    for tile_id in tiles.keys():
        if len(tiles[tile_id]['pairs']) == 2:
            corners.append(tile_id)
    return math.prod(corners)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    tiles = parse_input(file_path)
    answer = calculate_answer(tiles)
    print(answer)