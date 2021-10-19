#! /usr/bin/env python3

"""
Nested bags
"""

from pathlib import Path
import networkx as nx # networkx is our friend for this one.

p = Path(__file__).with_name('day07part1-input.txt')
# p = Path(__file__).with_name('day07part1-sample.txt')

with p.open('r') as f:
    lines = [l.strip() for l in f.readlines()]


# light red bags contain 1 bright white bag, 2 muted yellow bags.
# faded blue bags contain no other bags.

graph = nx.DiGraph()
token = 'bags contain'
for line in lines:
    token_index = line.find(token) 
    parent = line[:token_index-1] # -1 to trim space character
    children_str  = line[token_index+len(token)+1:] # +1 to trim space character
    if children_str == 'no other bags.':
        # Do we want to add parent to graph here, even though no children? Probably.
        continue
    for child_str in children_str.split(','):
        quantity, color1, color2, bag = child_str.split()
        child = ' '.join([color1, color2])
        graph.add_edge(parent, child)

outer_bags = nx.ancestors(graph, "shiny gold")

print(f'Number of bags that could contain shiny gold is {len(outer_bags)}')


