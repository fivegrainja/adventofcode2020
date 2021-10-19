#! /usr/bin/env python3

"""
How many passwords are valid according to their policies?
"""

from pathlib import Path

p = Path(__file__).with_name('day02part1-input.txt')
with p.open('r') as f:
    entries = f.readlines()

num_valid = 0
for entry in entries:
    parts = entry.split()
    min_num,max_num = (int(s) for s in parts[0].split('-'))
    char = parts[1][0]
    password = parts[2]
    if min_num <= list(password).count(char) <= max_num:
        num_valid += 1
print(num_valid)