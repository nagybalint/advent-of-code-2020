import os
from typing import Dict, List, Tuple

def parse_input(file_name: str) -> Dict[str, Dict[str, int]]:
    bags = {}
    with open(file_name) as in_file:
        for line in in_file.readlines():
            color, content = parse_bag(line.strip().replace(".", ""))
            bags[color] = content
    return bags

def parse_bag(line: str) -> Tuple[str, Dict[str, int]]:
    container, contents = line.split("contain")
    return parse_color(container.strip()), parse_contents(contents.strip())

def parse_color(container: str) -> str:
    return container[:-5]

def parse_contents(contents: str) -> Dict[str, int]:
    if contents == "no other bags":
        return {}
    content_dict = {}
    for content in contents.split(", "):
        parts = content.split(" ")
        amount = int(parts[0])
        color = " ".join(parts[1:3])
        content_dict[color] = amount
    return content_dict

def calculate_answer(bags: Dict[str, Dict[str, int]], color: str) -> int:
    containers = find_container_for(bags, color)
    containers.remove(color)
    return len(containers)

def find_container_for(bags: Dict[str, Dict[str, int]], color: str) -> List[str]:
    containers = set()
    containers.add(color)
    for k, v in bags.items():
        if color in v.keys():
            containers.add(k)
            new_containers = find_container_for(bags, k)
            containers = containers.union(new_containers)
    return containers

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    bags = parse_input(file_path)
    answer = calculate_answer(bags, "shiny gold")
    print(answer)