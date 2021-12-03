#! /usr/bin/env python3

# https://adventofcode.com/2021/day/1

import os

from itertools import combinations
from copy import deepcopy
from collections import Counter

def read_inputs(input):
    nums = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        for line in f.readlines():
            nums.append(line.strip())
    return nums


def solve(input):
    lines = read_inputs(input)
    x = 0
    y = 0
    for line in lines:
        parts = line.split(' ')
        val = int(parts[1])
        if parts[0] == 'forward':
            x += val
        elif parts[0] == 'down':
            y += val
        elif parts[0] == 'up':
            y -= val

    print(f"Answer part 1: {(x * y)}")

def solve2(input):
    lines = read_inputs(input)
    x = 0
    y = 0
    aim = 0
    for line in lines:
        parts = line.split(' ')
        val = int(parts[1])
        if parts[0] == 'forward':
            x += val
            y += (aim * val)
        elif parts[0] == 'down':
            aim += val
        elif parts[0] == 'up':
            aim -= val

    print(f"Answer part 2: {(x * y)}")

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")
