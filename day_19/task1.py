import os
from itertools import chain, groupby
from typing import Dict, List, Tuple

def parse_input(file_name: str) -> Tuple[List[str], List[str]]:
    rules = []
    messages = []
    with open(file_name) as f:
        rules, messages = [list(group) for k, group in groupby([line.strip() for line in f.readlines()], lambda x: x == "") if not k]
        return rules, messages

def collapse_rules(rules: List[str]) -> Dict[int, List[List[str]]]:
    def get_options_for_rule(num: str):
        if num in patterns:
            return

        pattern = raw_patterns[num]
        if pattern == '"a"' or pattern == '"b"':
            patterns[num] = [pattern[1]]
        else:
            patterns[num] = []
            for part in pattern.split(' | '):
                patterns_to_combine = []
                for embedded_rule in part.split(' '):
                    if not embedded_rule in patterns:
                        get_options_for_rule(embedded_rule)
                    patterns_to_combine.append(patterns[embedded_rule])
                patterns[num].extend(combine_patterns(patterns_to_combine))

    raw_patterns = {}
    for rule in rules:
        num, pattern = rule.split(': ')
        raw_patterns[num] = pattern
    
    patterns = {}
    for num, pattern in raw_patterns.items():
        get_options_for_rule(num)
    return patterns

def combine_patterns(p: List[List[str]]) -> List[str]:
    if len(p) == 1:
        return p[0]
    if len(p) == 2:
        return combine2(p[0], p[1])
    return combine2(p[0], combine_patterns(p[1:]))

def combine2(l_a, l_b):
    ret_val = []
    for a in l_a:
        for b in l_b:
            ret_val.append(f'{a}{b}')
    return ret_val

def calculate_answer(rules: List[str], messages: List[str]) -> int:
    patterns = collapse_rules(rules)
    options = set(patterns['0'])
    matching = []
    for m in messages:
        if m in options:
            matching.append(m)
    return len(matching)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    rules, messages = parse_input(file_path)
    answer = calculate_answer(rules, messages)
    print(answer)