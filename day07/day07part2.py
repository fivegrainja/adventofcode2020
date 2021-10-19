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

# Construct the graph
graph = nx.DiGraph()
token = 'bags contain'
for line in lines:
    token_index = line.find(token) 
    parent = line[:token_index-1] # -1 to trim space character
    children_str  = line[token_index+len(token)+1:] # +1 to trim space character
    if children_str == 'no other bags.':
        continue
    for child_str in children_str.split(','):
        q, color1, color2, bag = child_str.split()
        child = ' '.join([color1, color2])
        graph.add_edge(parent, child, quantity=int(q)) # Number of bags of this color is quantity attribute

# Recursive function to walk the downstream nodes of the parent counting all the bags it holds
def count_bags(g, parent):
    num_bags = 0
    for child in graph.successors(parent):
        # Add to num_bags however many bags of this child color it holds
        num_child = g.get_edge_data(parent, child)['quantity']
        # print(f'parent: {parent}  child: {child} - {num_child}')
        num_bags += num_child
        # Add the descendants of this child, remembering to multiply by how many of this child parent holds
        num_bags += num_child * count_bags(g, child)
    return num_bags

total_bags = count_bags(graph, "shiny gold")
print(f'Number of bags in a shiny gold bag is {total_bags}')





