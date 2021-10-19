#! /usr/bin/env python3

"""
Find the three entries that sum to 2020; what do you get if you multiply them together?
"""

import sys
from pathlib import Path

p = Path(__file__).with_name('day01part1-input.txt')
with p.open('r') as f:
    entries = f.readlines()
entries = [int(s) for s in entries]

for first_index,first in enumerate(entries[:-3]):
    for second_index,second in enumerate(entries[first_index+1:-2]):
        for third in entries[second_index+1:]:
            if first+second+third == 2020:
                print(f'{first}+{second}+{third}=2020')
                print(f'{first}*{second}*{third}={first*second*third}')
                sys.exit()
print('Finished without finding matching sum')