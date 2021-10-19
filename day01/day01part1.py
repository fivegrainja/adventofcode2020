#! /usr/bin/env python3

"""
Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

from pathlib import Path

p = Path(__file__).with_name('day01part1-input.txt')
with p.open('r') as f:
    entries = f.readlines()
entries = [int(s) for s in entries]

for index,first in enumerate(entries[:-2]):
    for second in entries[index+1:]:
        if first+second == 2020:
            print(f'{first}+{second}=2020')
            print(f'{first}*{second}={first*second}')
            break
    else:
        continue
    break
else:
    print('Finished without finding matching sum')