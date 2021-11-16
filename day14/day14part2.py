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
    p = Path(__file__).with_name('day14part2-sample.txt')
else:
    p = Path(__file__).with_name('day14part1-input.txt')

with p.open('r') as f:
    commands = [stripped_l for l in f.readlines() if (stripped_l:=l.strip()) != '']

memory = {}
mask = 'X' * 36

def apply_mask(address, mask):
    """ Returns a list of addresses
    """
    # Convert the address to a string representing the binary notation
    address = format(address, '0>36b') # 36 characters wide, padded on the left with zeros
    # Apply the 1's (0's are ignored in this question)
    address = list(address)
    for i, m in enumerate(mask):
        if m == '1':
            address[i] = '1'
        elif m == 'X':
            address[i] = 'X'
    address = ''.join(address)
    # Calculate all combinations for the X's
    def get_combinations(m):
        combinations = []
        i = m.find('X')
        if i == -1:
            combinations = [m]
        else:
            new_value = m.replace('X', '1', 1)
            combinations += get_combinations(new_value)
            new_value = m.replace('X', '0', 1)
            combinations += get_combinations(new_value)
        return combinations
    return get_combinations(address)
    
            
for c in commands:
    cmd, value = c.split('=')
    cmd = cmd.strip()
    value = value.strip()
    if cmd == 'mask':
        mask = value
    elif cmd.startswith('mem'):
        address = cmd.removeprefix('mem[')
        address = address.removesuffix(']')
        address = int(address)
        addresses = apply_mask(address, mask)
        for a in addresses:
            memory[a] = int(value)

big_sum = sum(memory.values())
print(f'{big_sum=}')


