#! /usr/bin/env python3

# https://adventofcode.com/2020/day/14

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


MASK = re.compile("mask = (.+)")
MEM = re.compile("mem\[(\d+)\] = (\d+)")

LENGTH = 36


def solve(input):
    memory = dict()
    for i in read_inputs(input):
        #print(i)
        if i.startswith("mask"):
            matches = MASK.match(i)
            mask = matches[1]
            bit_mask = [(index, bit) for index, bit in enumerate(mask) if bit != 'X']

        elif i.startswith("mem"):
            matches = MEM.match(i)
            address = int(matches[1])
            value = int(matches[2])
            binary_value = list(bin(value)[2:].zfill(LENGTH))
            # print("Before", ''.join(binary_value))

            for index, bit in bit_mask:
                binary_value[index] = bit
            masked_value = ''.join(binary_value)
            # print("After ", masked_value, int(masked_value, 2))

            memory[address] = int(masked_value, 2)

    print("[part 1]", sum(memory.values()))


def generate_address_combinations(masked_address):
    masked_address_list = list(masked_address)

    x_pairs = [(index, bit) for index, bit in enumerate(masked_address_list) if bit == 'X']

    x_count = masked_address.count('X')
    # 2^x_count
    for i in range(pow(2, x_count)):
        # 00, 01, 10, 11
        x_combination = bin(i)[2:].zfill(x_count)

        j = 0
        for index, _ in x_pairs:
            masked_address_list[index] = x_combination[j]
            j += 1
        yield ''.join(masked_address_list)

def solve2(input):
    memory = dict()
    for i in read_inputs(input):
        if i.startswith("mask"):
            matches = MASK.match(i)
            mask = matches[1]
            bit_mask = [(index, bit) for index, bit in enumerate(mask) if bit != '0']

        elif i.startswith("mem"):
            matches = MEM.match(i)
            address = int(matches[1])
            value = int(matches[2])
            binary_address = list(bin(address)[2:].zfill(LENGTH))
            # print("Before", ''.join(binary_address))

            for index, bit in bit_mask:
                binary_address[index] = bit
            masked_address = ''.join(binary_address)
            # print("After ", masked_address)

            # generate all combinations of addresses
            for address in generate_address_combinations(masked_address):
                # print(address, int(address, 2))
                memory[address] = value

    print("[part 2]", sum(memory.values()))

solve("in_short.txt")
#solve("in.txt")

solve2("in_short2.txt")
solve2("in.txt")
