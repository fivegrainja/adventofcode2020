#! /usr/bin/env python3

"""
Ferry movement
"""

from pathlib import Path
import sys
import math
from rich import print
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

waypoint_x = 10
waypoint_y = 1

ship_x = 0
ship_y = 0

def rotate(origin_x, origin_y, point_x, point_y, degrees):
    """ Returns new_point_x, new_point_y
    degrees is negative for clockwise rotation, positive for ccw.
    """
    angle = math.radians(degrees)

    new_x = origin_x + math.cos(angle) * (point_x - origin_x) - math.sin(angle) * (point_y - origin_y)
    new_y = origin_y + math.sin(angle) * (point_x - origin_x) + math.cos(angle) * (point_y - origin_y)
    return new_x, new_y

for action, amount in actions:
    match action:
        case 'N':
            waypoint_y += amount
        case 'S':
            waypoint_y -= amount
        case 'E':
            waypoint_x += amount
        case 'W':
            waypoint_x -= amount
        case 'L':
            waypoint_x, waypoint_y = rotate(ship_x, ship_y, waypoint_x, waypoint_y, amount)
        case 'R':
            waypoint_x, waypoint_y = rotate(ship_x, ship_y, waypoint_x, waypoint_y, -amount)
        case 'F':
            delta_x = (waypoint_x - ship_x) * amount
            delta_y = (waypoint_y - ship_y) * amount
            ship_x += delta_x
            ship_y += delta_y
            waypoint_x += delta_x
            waypoint_y += delta_y
        case _:
            print(f'Unrecognized action {action=}')
            sys.exit(-1)

manhattan = abs(ship_x) + abs(ship_y)
print(f'{manhattan=}')

