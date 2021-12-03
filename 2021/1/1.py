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
            nums.append(int(line))
    return nums


def solve(input):
    nums = read_inputs(input)
    counter = 0
    for i, n in enumerate(nums[1:], start=1):
        if (nums[i] > nums[i - 1]):
            counter += 1
    print(f"Answer part 1: {counter}")

def solve2(input):
    nums = read_inputs(input)
    sum = 0
    prev_sum = 0
    counter = 0
    for i, n in enumerate(nums[:-2]):
        sum = nums[i] + nums[i + 1] + nums[i + 2]
        if (prev_sum != 0 and sum > prev_sum):
            counter += 1
        prev_sum = sum

    print(f"Answer part 2: {counter}")

#solve("in_short.txt")
solve("in.txt")
#solve2("in_short.txt")
solve2("in.txt")
