#! /usr/bin/env python3

"""
Bit masking
"""

from pathlib import Path
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day14part1-sample.txt')
else:
    p = Path(__file__).with_name('day14part1-input.txt')

with p.open('r') as f:
    commands = [stripped_l for l in f.readlines() if (stripped_l:=l.strip()) != '']

memory = {}
mask = 'X' * 36

def apply_mask(value, mask):
    for i, m in enumerate(reversed(mask)):
        if m == '1':
            value |= pow(2,i)
        elif m == '0':
            value &= (pow(2, 37) - 1) - pow(2, i)
    return value

for c in commands:
    cmd, value = c.split('=')
    cmd = cmd.strip()
    value = value.strip()
    if cmd == 'mask':
        print(f'Setting mask to {value}')
        mask = value
    elif cmd.startswith('mem'):
        # Location can stay a string, it's just used as a key into memory.
        location = cmd.removeprefix('mem[')
        location = location.removesuffix(']')
        masked_value = apply_mask(int(value), mask)
        print(f'Applying mask of {mask} to {value} results in {masked_value}')
        memory[location] = masked_value

print(memory)
big_sum = sum(memory.values())
print(f'{big_sum=}')


