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
    orig_prog = [[line.split()[0],int(line.split()[1])] for line in f.readlines()]

def run_prog(prog):
    """ Return None if the program enters inifine loop. Return acc value if it terminates normally.
    """
    i = 0
    acc = 0
    previous_i = set()
    prog_len = len(prog)
    while True:
        if i == prog_len:
            # Normal program termination
            return acc
        if i in previous_i:
            # Inifine loop
            return None
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

# Run the program with different lines changed
for i, line in enumerate(orig_prog):
    if line[0] == 'nop':
        new_command = 'jmp'
    elif line[0] == 'jmp':
        new_command = 'nop'
    else:
        # We only try swapping nop and jmp commands and skip others
        continue
    # Create a shallow copy of orig_prog
    prog = [l for l in orig_prog]
    # Swap the command
    prog[i] = [new_command, prog[i][1]] # Careful to create a new list entry instead of modifying original
    result = run_prog(prog)
    if result is not None:
        # Program terminated normally
        print(f'Changed line {i}')    
        print(f'Value of accumulator is {result}')
        break



