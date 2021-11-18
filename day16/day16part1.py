#! /usr/bin/env python3

"""
Mystery tickets
"""

from pathlib import Path
import sys
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day16part1-sample.txt')
else:
    p = Path(__file__).with_name('day16part1-input.txt')

with p.open('r') as f:
    lines = [l.strip() for l in f.readlines()]

lines_iter = iter(lines)

# Read in the rules for the fields
rules = {}
for line in lines_iter:
    if not line:
        break
    field, bounds = line.split(':')
    range1, _, range2 = bounds.split()
    rules[field] = []
    for r in (range1, range2):
        lower, upper = r.split('-')
        rules[field].append(int(lower))
        rules[field].append(int(upper))
else:
    print('Problem reading rules')
    sys.exit(-1)

# Read our ticket
assert(next(lines_iter) == 'your ticket:')
my_ticket = next(lines_iter)
assert(next(lines_iter) == '')

# Read nearby tickets
nearby = []
assert(next(lines_iter) == 'nearby tickets:')
for line in lines_iter:
    nearby.append([int(f) for f in line.split(',')])

print(rules)
print(my_ticket)
print(nearby)

def check_validity(ticket, rules):
    # Returns True if the ticket is valid
    # Returns an integer (the invalid value from the ticket) if the ticket is invalid
    for value in ticket:
        for rule, ranges in rules.items():
            if (ranges[0] <= value <= ranges[1]) or (ranges[2] <= value <= ranges[3]):
                print(f'{value} falls within {ranges}')
                break
        else:
            print(f'Invalid {value}')
            return value
    return True

invalid_values = []
for ticket in nearby:
    value = check_validity(ticket, rules)
    if value != True:
        invalid_values.append(value)

print(f'Invalid values sum to {sum(invalid_values)}')


