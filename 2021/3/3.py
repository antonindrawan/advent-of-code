#! /usr/bin/env python3

# https://adventofcode.com/2021/day/3

import os
import numpy as np

from itertools import combinations
from copy import deepcopy
from collections import Counter

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

def get_gamma_epsilon(lines):
    n = len(lines[0])
    zeros = [0] * n
    ones = [0] * n
    for line in lines:
        for i, c in enumerate(line):
            if (c == '0'):
                zeros[i] += 1
            else:
                ones[i] += 1

    gamma_rate = ""
    epsilon_rate = ""
    for i in range(n):
        if zeros[i] > ones[i]:
            gamma_rate += '0'
            epsilon_rate += '1'
        #elif zeros[i] < ones[i]:
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    return gamma_rate, epsilon_rate


def solve(input):
    lines = read_inputs(input)
    gamma_rate, epsilon_rate = get_gamma_epsilon(lines)
    print(f"Answer part 1: {(int(gamma_rate, 2) * int(epsilon_rate, 2))}")

def get_oxygen_or_co2(lines_input, gamma):
    lines = lines_input.copy()
    i = 0
    while (len(lines) > 1):
        gamma_rate, epsilon_rate = get_gamma_epsilon(lines)

        temp_lines = []
        for line in lines:
            if gamma == True and gamma_rate[i] == line[i]:
                temp_lines.append(line)
            elif gamma == False and epsilon_rate[i] == line[i]:
                temp_lines.append(line)

        lines = temp_lines.copy()
        i += 1
    return lines[0]

def solve2(input):
    lines = read_inputs(input)

    oxygen = get_oxygen_or_co2(lines, gamma=True)
    co2 = get_oxygen_or_co2(lines, gamma=False)
    print(f"Answer part 2: {(int(oxygen, 2) * int(co2, 2))}")

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")