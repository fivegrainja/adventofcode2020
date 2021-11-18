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
my_ticket = [int(i) for i in my_ticket.split(',')]
assert(next(lines_iter) == '')

# Read nearby tickets
nearby = []
assert(next(lines_iter) == 'nearby tickets:')
for line in lines_iter:
    nearby.append([int(f) for f in line.split(',')])

def check_validity(ticket, rules):
    # Returns True if the ticket is valid
    # Returns an integer (the invalid value from the ticket) if the ticket is invalid
    for value in ticket:
        for rule, ranges in rules.items():
            if (ranges[0] <= value <= ranges[1]) or (ranges[2] <= value <= ranges[3]):
                # print(f'{value} falls within {ranges}')
                break
        else:
            # print(f'Invalid {value}')
            return value
    return True

invalid_values = []
valid_tickets = [my_ticket]
for ticket in nearby:
    value = check_validity(ticket, rules)
    if value != True:
        invalid_values.append(value)
    else:
        valid_tickets.append(ticket)

print(f'Invalid values sum to {sum(invalid_values)}')


# field_options contains items field:possible_columns where field is the field name and possible_columns
# is a set containing the possible field numbers in the ticket that the field matches.
field_options = {}
field_values = list(zip(*valid_tickets, strict=True))
for field_name, ranges in rules.items():
    field_options[field_name] = set()
    for i, values in enumerate(field_values):
        for v in values:
            if not (ranges[0] <= v <= ranges[1] or ranges[2] <= v <= ranges[3]):
                # We fould a value in this field index that does not match the ranges for this field name
                break
        else:
            # All the values in this field index matched the ranges for this field name
            field_options[field_name].add(i)

field_options = list(field_options.items())
field_options.sort(key=lambda x: len(x[1]))
print(field_options)

results = {}
previously_used = set()
for field_name, field_indexes in field_options:
    field_index = field_indexes - previously_used
    if len(field_index) != 1:
        print('Problem')
        sys.exit(-1)
    results[field_name] = field_index.pop()
    previously_used.add(results[field_name])

# print(results)

result = 1
for field_name, field_index in results.items():
    if field_name.startswith('departure'):
        result *= my_ticket[field_index]

print(result)

# NOT 930240