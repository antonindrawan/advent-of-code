"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

lr -> 1 wb, 2 yb
do -> 3 wb. 4 yb
bw -> 1 sg
my -> 2 sg, 9 fb

"""

import re

#from anytree import Node, RenderTree, AsciiStyle
#import anytree.search

RULE_PTR = re.compile("^(.+) bags contain (.*)")
CHILD_PTR = re.compile("(([0-9]?) (.+?)) bags?(?:,\s|\.|$)")


class Node:
    name = ""
    def __init__(self, name):
        self.name=name
        self.children = []

def read_inputs(input):
    #root = Node("*")

    bags = dict()
    with open(input, "r") as f:
        lines = (line.strip() for line in f.readlines())
    for line in lines:
        groups = RULE_PTR.match(line)
        node_name = groups[1]
        # print(f" [1] {node_name}")

        node = Node(node_name)
        assert node_name not in bags

        children = []
        if "no other bags." not in groups[2]:
            for matches in re.finditer(CHILD_PTR, groups[2]):
                child_node_name = matches.group(3)
                child_node_amount = matches.group(2)
                # print(f"  children: {child_node_amount} . {child_node_name}")
                child = (child_node_name, child_node_amount)
                children.append(child)
        bags[node_name] = children

    #for key, val in bags.items():
    #    print(key)
    #    for child in val:
    #        print(f" -> {child[0]}, {child[1]}")
    return bags


def solve1(input):
    bags = read_inputs(input)
    result = solution1(bags, "shiny gold")
    print(f"[part 1] {result}")


def has_named_child(bags, bag_name, target):
    found = False
    for bag in bags[bag_name]:
        if bag[0] == target:
            found = True
            break
        else:
             found = has_named_child(bags, bag[0], target)
             if found:
                 break

    return found

def solution1(bags, target):
    count = 0
    for key in bags.keys():
        if key != target:
            if has_named_child(bags, key, target):
                #print(f"has shiny gold: {key}")
                count += 1
    return count

def calculate_cost(bags, target):
    #print(f"target: {target}")
    result = 0
    if len(bags[target]) == 0:
        return 0
    for bag in bags[target]:
        cost = calculate_cost(bags, bag[0]) * int(bag[1]) + int(bag[1])
        print(f"{bag} cost = {cost}")
        result += cost

    return result


"""
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags. ->
dark orange bags contain 2 dark yellow bags. -> 31
dark yellow bags contain 2 dark green bags. -> 15
dark green bags contain 2 dark blue bags. -> 7
dark blue bags contain 2 dark violet bags. -> 3
dark violet bags contain no other bags. 1
"""

def solve2(input):
    bags = read_inputs(input)
    cost = calculate_cost(bags, "shiny gold")
    print(cost)


solve1("in.txt")
solve1("in_short2.txt")
solve2("in_short2.txt")
solve2("in.txt")