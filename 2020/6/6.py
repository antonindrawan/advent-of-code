#! /usr/bin/env python3

import collections

def read_inputs(input):
    lines = []
    with open(input, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def solve1(input):
    groups = []
    char_set = set()
    lines = read_inputs(input)
    for line in lines:
        if not line:
            groups.append(char_set)
            char_set = set()
        else:
            for c in line:
                char_set.add(c)
    groups.append(char_set)
    print(f"[part 1] {sum(map(len, groups))}")


def get_count(group):
    size = len(group)

    if size == 1:
        return len(group[0])

    dict_a = dict()
    for item in group:
        for c in item:
            if c in dict_a:
                dict_a[c] += 1
            else:
                dict_a[c] = 1

    count = 0
    for _, val in dict_a.items():
        if val == size:
            count += 1

    return count


def solve2(input):
    lines = read_inputs(input)
    result = []
    group = []
    for line in lines:
        if not line:
            count = get_count(group)
            #print(f"{count} = {group}")
            result.append(count)
            group = []
        else:
            line = ''.join(sorted(line))
            group.append(line)

    count = get_count(group)
    #print(f"{count} = {group}")
    result.append(count)
    print(f"[part 2] {sum(result)}")

solve1("in_short.txt")
solve1("in.txt")
solve2("in_short.txt")
solve2("in.txt")
