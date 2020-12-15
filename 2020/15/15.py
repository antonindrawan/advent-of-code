#! /usr/bin/env python3

# https://adventofcode.com/2020/day/15

import os, re

from itertools import combinations_with_replacement, combinations
from copy import deepcopy
from collections import Counter




def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def solution(input, max_turn):
    for input in read_inputs(input):
        numbers = dict()
        sequence = [int(x) for x in input.split(',')]
        sequence_len = len(sequence)

        for i in range(sequence_len - 1): # exclude the last one
            numbers[sequence[i]] = i + 1

        current_turn = sequence_len + 1
        last_number = sequence[-1]

        while (current_turn <= max_turn):
            if last_number in numbers:
                new_number = (current_turn - 1) - numbers[last_number]
                numbers[last_number] = current_turn - 1

                last_number = new_number

            else:
                numbers[last_number] = sequence_len
                last_number = 0

            #sequence.append(last_number)
            sequence_len += 1

            #print(numbers, sequence)
            #print(f"Turn {current_turn}; last_number = {last_number}")
            #print()
            current_turn += 1

        print(f"Turn {current_turn-1}; last_number = {last_number}")


def solve(input):
    solution(input, 2020)

def solve2(input):
    solution(input, 30000000)


#solve("in_short.txt")
solve("in.txt")
#solve2("in_short.txt")
solve2("in.txt")
