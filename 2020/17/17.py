#! /usr/bin/env python3

# https://adventofcode.com/2020/day/17

import os, re, sys
from itertools import product
import operator

ACTIVE = '#'
INACTIVE = '.'

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def solve(input):
    inputs = read_inputs(input)
    row_count = len(inputs)
    assert len(inputs[0]) == row_count

    cubes = {}
    for i in range(row_count):
        for j in range(row_count):
            coordinates = (i,j,0)
            if inputs[i][j] == '#':
                cubes[coordinates] = 1
    cubes_count = count_active_cubes(cubes, row_count, iteration=6)
    print("[part 1] Active cubes after 6 cycles:", cubes_count)

def count_active_cubes(cubes, cube_size, iteration):
    z_count = 1
    z_count = 1
    neighbors_deltas = list(product((-1, 0, 1), repeat=3))

    for _ in range(iteration):
        new_cubes = {}
        for i in range(-iteration, cube_size + iteration):
            for j in range(-iteration, cube_size + iteration):
                for z in range(-iteration, z_count + iteration):
                    coordinate = (i, j, z)
                    active_neighbors = 0
                    for d in neighbors_deltas:
                        neigbor = tuple(map(operator.add, d, coordinate))
                        if neigbor != coordinate and neigbor in cubes and cubes[neigbor] == 1:
                            active_neighbors += 1
                    #print(coordinate, active_neighbors)
                    if coordinate in cubes:
                        if active_neighbors >= 2 and active_neighbors <= 3:
                            new_cubes[coordinate] = 1
                    elif active_neighbors == 3:
                        new_cubes[coordinate] = 1
        cubes = new_cubes
        print(new_cubes)
        print(len(cubes))
    return len(cubes)


    # new_cubes = {}
    # for coordinate, val in cubes.items():
    #     print(coordinate)
    #     active_neighbors = 0
    #     for d in neighbors_deltas:
    #         neigbor = tuple(map(operator.add, d, coordinate))
    #         if neigbor != coordinate and neigbor in cubes and cubes[neigbor] == 1:
    #             active_neighbors += 1
    #     print(active_neighbors)
    #     if val == 1 and (active_neighbors >= 2 and active_neighbors <= 3):
    #         new_cubes[coordinate] = 1
    #     elif val == 0 and active_neighbors == 3:
    #         new_cubes[coordinate] = 1
    #     else:
    #         new_cubes[coordinate] = 0


    # print(new_cubes)

solve("in_short.txt")
solve("in.txt")