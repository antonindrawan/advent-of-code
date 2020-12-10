#! /usr/bin/env python3

import os
import sys

from itertools import combinations
from collections import Counter

precomputed_numbers = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6: 24}


def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [int(line) for line in f.readlines()]
    return lines

def get_diff(input):
    data = read_inputs(input)
    data = sorted(data)
    built_in_jolt = max(data) + 3
    data.insert(0, 0)
    data.append(built_in_jolt)

    diff = [data[x] - data[x-1] for x in range(1, len(data))]
    return diff

def solve(input):
    diff = get_diff(input)
    diff_counter = Counter(diff)
    print(f"[part 1] 1-jolt x 3-jolt = {diff_counter[1] * diff_counter[3]}")


def solve2(input):
    diff = get_diff(input)
    result = 1
    count = 0
    max_count = 0
    for i in range(len(diff) - 1, -1, -1):
        if diff[i] == 1:
            count += 1
        else:
            #if max_count < count:
            max_count = max(max_count, count)
            try:
                result *= precomputed_numbers[count]
            except KeyError as e:
                sys.exit(f"Unsupported precomputed number -> KeyError: {e}")
            count = 0

    max_count = max(max_count, count)
    result *= precomputed_numbers[count]
    print(f"[part 2] {result}. Max consecutive '1's is {max_count}")

solve("in_short.txt")
solve("in_short2.txt")
solve("in.txt")

solve2("in_short.txt")
solve2("in_short2.txt")
solve2("in.txt")

"""
1, 3, 2, 1, 3, 1, 1, 3, 1, 3, 3
1, 1, 2, 1
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)



####
1, 3, 1, 2, 3, 1, 1, 3, 1, 3
1, 1, 2, 1 = 4

(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)


, 1, 3, 5, 7, 10, 12, 15, 16, 19, (22)

4, 5, 6, 7 = 1 1 1 => 3 * '1' = 4
4, 5, 7
4, 6, 7
4, 7


4, 5, 6, 7, 8 = 1 1 1 1 => 4 * '1' = 7
4, 5, 6, 8
4, 5, 7, 8
4, 6, 7, 8
4, 5, 8
4, 6, 8
4, 7, 8

4, 5, 6, 7, 8, 9 = 5 * '1' = 13
4, 5, 6, 7, 9
4, 5, 6, 8, 9
4, 5, 7, 8, 9
4, 6, 7, 8, 9

4, 5, 6, 9
4, 5, 7, 9
4, 5, 8, 9
4, 6, 7, 9
4, 6, 8, 9
4, 7, 8, 9
4, 6, 9
4, 7, 9



4, 5, 6, 7, 8, 9, 10 = 6 * '1' = 24
4, 5, 6, 7, 8, 10
4, 5, 6, 7, 9, 10
4, 5, 6, 8, 9, 10
4, 5, 7, 8, 9, 10
4, 6, 7, 8, 9, 10
4, 5, 6, 7, 10
4, 5, 6, 8, 10
4, 5, 7, 8, 10
4, 6, 7, 8, 10
4, 5, 6, 9, 10
4, 5, 7, 9, 10
4, 6, 7, 9, 10
4, 5, 8, 9, 10
4, 6, 8, 9, 10
4, 7, 8, 9, 10
4, 5, 7, 10
4, 6, 7, 10
4, 5, 8, 10
4, 6, 8, 10
4, 7, 8, 10
4, 6, 9, 10
4, 7, 9, 10
4, 7, 10


n = 6
6 => 5 (n-1)
5 => 10 (4 + 3 + 2 + 1)
4 => 5 (2 + 2 + 1)
3 => 1

####
[1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3]
Count consecutive '1': 4, 4, 3, 2, 4, 1, 4

7*7*2*4*7*7 = 19208

Pattern:
2*'1' = 2
3*'1' = 4
4*'1' = 7
5*'1' = 13
6*'1' = 24
"""