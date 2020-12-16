import math
import os
from typing import Callable, Dict, IO, List, Tuple
from task1 import parse_input

def calculate_answer(rules: Dict[str, Callable[[int], bool]], tickets: List[List[int]]) -> int:
    own_ticket = tickets[0]
    nearby_tickets = tickets[1:]
    valid_tickets = discard_invalid_tickets(rules, nearby_tickets)
    field_candidates = find_field_candidates(valid_tickets, rules)
    final_field_indices = finalize_fields(field_candidates)

    return math.prod([
        own_ticket[i] for i in [
            i for name, i in final_field_indices.items() if name.startswith("departure")]])

def finalize_fields(field_candidates):
    final_field_indices = {}
    while True:
        for i, c in enumerate(field_candidates):
            if len(c) == 1:
                final_field_indices[c[0]] = i
                remove_candidate(field_candidates, c[0])
                break
        else:
            break
    return final_field_indices

def find_field_candidates(tickets, rules):
    field_candidates = []
    ticket_length = len(tickets[0])
    for i in range(ticket_length):
        field_candidates.append([])
        vals_at_i = [ticket[i] for ticket in tickets]
        for name, f in rules.items():
            if all([f(v) for v in vals_at_i]):
                field_candidates[-1].append(name)
    return field_candidates

def remove_candidate(field_candidates: List[List[str]], c):
    for cand in field_candidates:
        try:
            cand.remove(c)
        except:
            pass

def discard_invalid_tickets(rules, tickets) -> List[List[int]]:
    validators = rules.values()
    valid_tickets = []
    for ticket in tickets:
        for val in ticket:
            validities = [f(val) for f in validators]
            if not any(validities):
                break
        else:
            valid_tickets.append(ticket)
    return valid_tickets

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    rules, tickets = parse_input(file_path)
    answer = calculate_answer(rules, tickets)
    print(answer)