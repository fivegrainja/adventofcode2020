#! /usr/bin/env python3

"""
Conway's cubes
"""

from pathlib import Path
from collections import deque
import sys
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
TEST = True

if TEST:
    p = Path(__file__).with_name('day17part1-sample.txt')
else:
    p = Path(__file__).with_name('day17part1-input.txt')

with p.open('r') as f:
    lines = [l.strip() for l in f.readlines()]

num_rounds = 6
width = len(lines[0]) + 2 * num_rounds
height = 1 + (2 * num_rounds)

print(f'{width=}')
print(f'{height=}')

stack = [[['.' for c in range(width)] for r in range(width)] for h in range(height)]

print(f'stack height is {len(stack)}')
print(f'Stack rows is {len(stack[0])}')
print(f'Stack cols is {len(stack[0][0])}')

# Initial population
z = num_rounds
for line_number, line in enumerate(lines):
    for cell_number, cell in enumerate(line):
        breakpoint()
        stack[z][num_rounds+line_number][num_rounds+cell_number] = cell
print(stack)