#! /usr/bin/env python3

"""
How many valid passports?
"""

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

from pathlib import Path

p = Path(__file__).with_name('day04part1-input.txt')
with p.open('r') as f:
    lines = f.readlines()

# Build a list of all passports in the data
# Line by line accumulate data into a passport until a blank line is encountered,
# then start a new passport
passports = []
passport = {}
for line in lines:
    if line.strip():
        for part in line.split():
            k,v = part.split(':')
            if k in passport:
                raise 'Problem'
            passport[k] = v
    elif passport:
        passports.append(passport)
        passport = {}
# Make sure to include the last passport, which might not be followed
# by a blank line.
if passport:
    passports.append(passport)


def validate(p):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    try:
        byr = int(p['byr'])
    except ValueError:
        return False
    if byr < 1920 or byr > 2002:
        return False
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    try:
        iyr = int(p['iyr'])
    except ValueError:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    try:
        eyr = int(p['eyr'])
    except ValueError:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    unit = p['hgt'][-2:]
    try:
        hgt = int(p['hgt'][:-2])
    except ValueError:
        return False
    if unit == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    elif unit == 'in':
        if hgt < 59 or hgt > 76:
            return False
    else:
        raise f'Unrecognized unit {unit}'
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if len(p['hcl']) != 7 or not p['hcl'].startswith('#'):
        return False
    if not set(p['hcl'][1:]).issubset('0123456789abcdef'):
        return False
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if p['ecl'] not in ('amb','blu','brn','gry','grn','hzl','oth'):
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(p['pid']) != 9:
        return False
    try:
        int(p['pid'])
    except ValueError:
        return False
    return True
    
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid = [p for p in passports
            if required.issubset(p.keys())
            and validate(p)]
print(f'Num valid is {len(valid)}')
