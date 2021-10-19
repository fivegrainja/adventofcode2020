#! /usr/bin/env python3

"""
Product of the number of trees hit for each given slope
"""

from pathlib import Path

p = Path(__file__).with_name('day03part1-input.txt')
with p.open('r') as f:
    pattern = [l.strip() for l in f.readlines() if l]

# (places to the right, lines down)
slopes = (
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
)

line_length = len(pattern[0])
product = 1

for move_right,move_down in slopes:
    position = 0
    num_trees = 0
    for line_num in range(0, len(pattern), move_down):
        line = pattern[line_num]
        if line[position] == '#':
            num_trees += 1
        position = (position + move_right) % line_length
    product *= num_trees
print(f'Product of hit trees is {product}')