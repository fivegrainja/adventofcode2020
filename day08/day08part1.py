#! /usr/bin/env python3

"""
Code interpreter
"""

from pathlib import Path
import sys

p = Path(__file__).with_name('day08part1-input.txt')
# p = Path(__file__).with_name('day08part1-sample.txt')

with p.open('r') as f:
    # Each element in the program is (cmd, arg) where cmd is string and arg is int
    prog = [(line.split()[0],int(line.split()[1])) for line in f.readlines()]

i = 0
acc = 0
previous_i = set()
while True:
    if i in previous_i:
        break
    previous_i.add(i)
    cmd, arg = prog[i]
    if cmd == 'acc':
        acc += arg
        i += 1
    elif cmd == 'jmp':
        i += arg
    elif cmd == 'nop':
        i += 1
    else:
        print(f'Encountered unknown command: {cmd}')
        sys.exit(-1)

print(f'Value of accumulator is {acc}')



