#! /usr/bin/env python3

# https://adventofcode.com/2020/day/23

import os
from copy import deepcopy


class Node:
    def __init__(self, number):
        self.number = number
        self.next = None


def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        numbers = [int(num) for num in f.readline()]
    return numbers


def solve(input):
    lookup_nodes = solution(input, 9, 100)
    print("[part 1] ", end='')
    node = lookup_nodes[1]
    for i in range(8):
        node = node.next
        print(node.number, end='')
    print()


def get_destination(current_node, pick_up_nodes, max_number):
    destination = current_node.number - 1
    if destination == 0:
        destination = max_number
    while destination in [node.number for node in pick_up_nodes]:
        destination -= 1
        if destination == 0:
            destination = max_number
    return destination


def move_cycle(lookup_nodes, start_node, cycles):
    nodes_count = len(lookup_nodes) - 1
    cycle = 0
    current_node = start_node
    while cycle < cycles:
        pick_up_nodes = [current_node.next, current_node.next.next, current_node.next.next.next]

        destination = get_destination(current_node, pick_up_nodes, nodes_count)
        destination_node = lookup_nodes[destination]
        destination_next_node = destination_node.next

        # set the next node of the current to the next node of the last pick up node
        # 3 -> 8 -> 9 -> 1 -> 2..
        # pick up nodes: 8 -> 9 -> 1
        # becomes: 3 -> 2 after shifting the picked up nodes
        current_node.next = pick_up_nodes[-1].next

        # Set the current node for the next cycle, before it is updated
        current_node = current_node.next

        # Set the pick up nodes to be the next node of the destination node
        destination_node.next = pick_up_nodes[0]

        # Update the next node of the last node in the pick up nodes
        pick_up_nodes[-1].next = destination_next_node

        cycle += 1


def solution(input, max_number, cycles):
    input_numbers = read_inputs(input)

    lookup_nodes = []
    for _ in range(len(input_numbers)+1):
        lookup_nodes.append(Node(-1))

    for num in range(len(input_numbers)+1, max_number+1):
        input_numbers.append(num)
        lookup_nodes.append(Node(-1))

    first_node = Node(input_numbers[0])
    lookup_nodes[input_numbers[0]] = first_node

    previous_node = first_node
    for idx in range(1, len(input_numbers)):
        num = input_numbers[idx]
        node = Node(num)
        previous_node.next = node
        lookup_nodes[num] = node
        previous_node = node
    node.next = first_node

    move_cycle(lookup_nodes, first_node, cycles)
    return lookup_nodes


def solve2(input):
    lookup_nodes = solution(input, 1000000, 10000000)
    node_one = lookup_nodes[1]
    print("[part 2] Result", node_one.next.number * node_one.next.next.number)

#solve("in_short.txt")
solve("in.txt")

#solve2("in_short.txt")
solve2("in.txt")

