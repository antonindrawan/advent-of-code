#! /usr/bin/env python3

# https://adventofcode.com/2020/day/25

import os

DIVIDER = 20201227

def read_inputs(input):
    public_keys = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        public_keys.append(int(f.readline()))
        public_keys.append(int(f.readline()))
    return public_keys

def determine_loop_size(subject_number):
    return subject_number


def transform(value, subject_number):
    return (value * subject_number) % 20201227


def solve(input):
    public_keys = read_inputs(input)

    loop_sizes = []
    for public_key in public_keys:
        loop_size = 0
        value = 1
        while value != public_key:
            value = transform(value, 7)
            loop_size += 1
        loop_sizes.append(loop_size)

    value = 1
    for _ in range(loop_sizes[0]):
        value = transform(value, public_keys[1])
    public_keys[1] = value
    print("[Part 1]", value)

solve("in_short.txt")
solve("in.txt")

# There is no part 2 (DONE)