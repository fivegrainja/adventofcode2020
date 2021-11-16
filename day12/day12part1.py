#! /usr/bin/env python3

"""
Ferry movement
"""

from pathlib import Path
import sys
from rich import print
from collections import deque
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day12part1-sample.txt')
else:
    p = Path(__file__).with_name('day12part1-input.txt')

with p.open('r') as f:
    actions = [(s[0], int(s[1:])) for l in f.readlines() if (s:=l.strip()) != '']

# The first item in compass indicates what direction the ferry is pointed.
# Turning to the left involves rotating compass to the left
# Turning to the right involves rotating the compass to the right
# If the compass is 'E', 'N', 'W', 'S' and you need to turn 270 degrees to the left:
# -- 270/90=3 which is how many places to rotate compass
# -- turning to the left means rotating compass to the left
# compass.rotate(-3), which results in 'S', 'E', 'N', 'W' (ferry is now pointing S)
# Note: it's important that the letters in the compass match the directional commands in the 
# input actions, because we translate the F command (forward) to being movement in the direction
# compass[0]
compass = deque(['E', 'N', 'W', 'S'])

def turn_left(compass, degrees):
    turns = int(degrees/90)
    compass.rotate(-turns)

def turn_right(compass, degrees):
    turns = int(degrees/90)
    compass.rotate(turns)

position_x = 0
position_y = 0

for action, amount in actions:
    if action == 'F':
        action = compass[0]
    match action:
        case 'N':
            position_y += amount
        case 'S':
            position_y -= amount
        case 'E':
            position_x += amount
        case 'W':
            position_x -= amount
        case 'L':
            turn_left(compass, amount)
        case 'R':
            turn_right(compass, amount)
        case _:
            print(f'Unrecognized action {action=}')
            sys.exit(-1)

manhattan = abs(position_x) + abs(position_y)
print(f'{manhattan=}')

