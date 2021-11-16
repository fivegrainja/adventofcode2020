#! /usr/bin/env python3

"""
Seating evolution
"""

from pathlib import Path
from rich import print
import rich.traceback
rich.traceback.install(show_locals=True)

TEST = False
# TEST = True

if TEST:
    p = Path(__file__).with_name('day11part1-sample.txt')
else:
    p = Path(__file__).with_name('day11part1-input.txt')

with p.open('r') as f:
    # My first time using an assignment expression in a list comprehension,
    # I'm pretty excited about this.
    seats = [list(row) for l in f.readlines() if (row:=l.strip()) != '']

print('Initial seating')
print(seats)

def count_visible_occupied_seats(seats, row, col):
    """ Return the number of directions (left, right, above, below, diagonals) in which the first
    visible seat (so skipping spaces) is occupied

    So turns out this takes a bit of time to run (a minute maybe on my laptop.)
    A potential improvement would be to not calculate the seats in each
    direction for each seat each round on the fly as below. Instead, at the start, for each seating
    position create 8 list - one for each direction from that seat (fewer for edge seats maybe.) Each list
    is the seating positions going out in that direction from that seat, in order.
    """
    num_visible_occupied = 0
    # Left
    for c in range(col-1, -1, -1):
        if seats[row][c] != '.':
            if seats[row][c] == '#':
                num_visible_occupied += 1
            break
    # Right
    for c in range(col+1,len(seats[row])):
        if seats[row][c] != '.':
            if seats[row][c] == '#':
                num_visible_occupied += 1
            break
    # Above
    for r in range(row-1, -1, -1):
        if seats[r][col] != '.':
            if seats[r][col] == '#':
                num_visible_occupied += 1
            break
    # Below
    for r in range(row+1, len(seats)):
        if seats[r][col] != '.':
            if seats[r][col] == '#':
                num_visible_occupied += 1
            break
    
    # Upper left diagonal
    r = row - 1
    c = col - 1
    while (r >= 0 and c >= 0):
        if seats[r][c] != '.':
            if seats[r][c] == '#':
                num_visible_occupied += 1
            break
        r -= 1
        c -= 1

    # Upper right diagonal
    r = row - 1
    c = col + 1
    while (r >= 0 and c < len(seats[0])):
        if seats[r][c] != '.':
            if seats[r][c] == '#':
                num_visible_occupied += 1
            break
        r -= 1
        c += 1
    
    # Lower left diagonal
    r = row + 1
    c = col - 1
    while (r < len(seats) and c >= 0):
        if seats[r][c] != '.':
            if seats[r][c] == '#':
                num_visible_occupied += 1
            break
        r += 1
        c -= 1

    # Lower right diagonal
    r = row + 1
    c = col + 1
    while (r < len(seats) and c < len(seats[0])):
        if seats[r][c] != '.':
            if seats[r][c] == '#':
                num_visible_occupied += 1
            break
        r += 1
        c += 1

    return num_visible_occupied


def get_next_round(seats):
    """ Takes an array of seats, constructs an array representing seating for the next round
    according to the rules of the question.
    Returns a tuple (next_seats, is_different) where next_seats is the next round of seats
    and is_different is a boolean indicating whether any seats changed between seats and next_seats.
    """
    next_seats = []
    is_different = False
    for row in range(len(seats)):
        next_seats.append([])
        for col in range(len(seats[row])):
            this_seat = seats[row][col]
            # Default condition is for the seat's state not to change
            this_seat_becomes = this_seat
            if this_seat == 'L':
                if count_visible_occupied_seats(seats, row, col) == 0:
                    this_seat_becomes = '#'
            elif this_seat == '#':
                if count_visible_occupied_seats(seats, row, col) >= 5:
                    this_seat_becomes = 'L'
            if this_seat != this_seat_becomes:
                is_different = True
            next_seats[row].append(this_seat_becomes)
    return (next_seats, is_different)

is_different = True
while (is_different):
    seats, is_different = get_next_round(seats)
    print(seats)

print('Final seating')
print(seats)

num_occupied = 0
for row in seats:
    num_occupied += row.count('#')
print(f'{num_occupied=}')

            


