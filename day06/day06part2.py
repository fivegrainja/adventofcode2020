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
            # We encountered a line that wasn't blank and we aren't currently working with an
            # existing group (this_group), so create a new group using this line.
            this_group = set(line)
        else:
            # We have a current this_group.
            # Update this_group to be the intersection of itself and this line
            this_group = this_group.intersection(line)
    elif this_group is not None: # Careful - we want to handle empty set and None differently
        # We encountered a blank line and have a current this_group so
        # add this_group to all_groups and set this_group
        # close out the group by setting this_group to None. If we encounter
        # another group then a new this_group will be created for it above.
        all_groups.append(this_group)
        this_group = None
if this_group is not None:
    all_groups.append(this_group)

sum = 0
for group in all_groups:
    sum += len(group)

print(f'Sum is {sum}')