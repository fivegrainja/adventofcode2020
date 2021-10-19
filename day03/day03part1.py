#! /usr/bin/env python3

"""
How many trees would be hit in the pattern?
"""

from pathlib import Path

p = Path(__file__).with_name('day03part1-input.txt')
with p.open('r') as f:
    pattern = [l.strip() for l in f.readlines() if l]

line_length = len(pattern[0])
slope = 3
position = 0
num_trees = 0
for line_num, line in enumerate(pattern):
    if line[position] == '#':
        num_trees += 1
    position = (position + slope) % line_length
print(f'Hit {num_trees} trees')