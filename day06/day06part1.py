#! /usr/bin/env python3

"""
Count unique answers within group
"""

from pathlib import Path

p = Path(__file__).with_name('day06part1-input.txt')
# p = Path(__file__).with_name('day06part1-sample.txt')

with p.open('r') as f:
    lines = [l.strip() for l in f.readlines()]

all_groups = []
this_group = None
for line in lines:
    if line.strip():
        if this_group is None:
            # We encountered a line that wasn't blank, but we don't have
            # a this_group, so create a this_group and add it to the list
            # of all groups
            this_group = set()
            all_groups.append(this_group)
        # Add all letters from this line to the current this_group
        this_group.update(list(line))
    elif this_group:
        # We encountered a blank line and have a current this_group, so
        # close out the group by setting this_group to None. If we encounter
        # another group then a new this_group will be created for it above.
        this_group = None

# from pprint import pprint
# pprint(all_groups)

sum = 0
for group in all_groups:
    sum += len(group)

print(f'Sum is {sum}')