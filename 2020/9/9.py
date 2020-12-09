#! /usr/bin/env python3

# https://adventofcode.com/2020/day/9

import os

from itertools import combinations
from copy import deepcopy


def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [int(line) for line in f.readlines()]
    return lines


def find_invalid_number(inputs, preamble):
    for i in range(preamble, len(inputs)):
        items = [inputs[x] for x in range(i - preamble, i)]
        #print(items)
        found = False
        for x in combinations(items, 2):
            if (x[0] + x[1]) == inputs[i]:
                found = True
                break

        if not found:
            return inputs[i], i


def find_sub_array_equals_number(inputs, invalid_number):
    n = len(inputs)
    dp = inputs.copy()

    sum = 0
    for i in range(0, n):
        sum += inputs[i]
        dp[i] = sum
    for i in range(1, n):
        for j in range(0, i):
            if dp[i]-dp[j] == invalid_number:
                return [inputs[i] for i in range(j + 1, i + 1)]


def solve(input, preamble):
    inputs = read_inputs(input)
    invalid_number, i = find_invalid_number(inputs, preamble)
    print(f"[part 1] Invalid number: {invalid_number} found at {i}")


def solve2(input, preamble):
    inputs = read_inputs(input)
    invalid_number, _ = find_invalid_number(inputs, preamble)
    sub_array = find_sub_array_equals_number(inputs, invalid_number)
    print(f"[part 2] Encryption weakness: {min(sub_array) + max(sub_array)}")


solve("in_short.txt", 5)
solve2("in_short.txt", 5)

solve("in.txt", 25)
solve2("in.txt", 25)

