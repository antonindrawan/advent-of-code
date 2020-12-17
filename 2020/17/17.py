#! /usr/bin/env python3

# https://adventofcode.com/2020/day/17

import os, re, sys
from itertools import product
import operator

ACTIVE = '#'
INACTIVE = '.'

def read_inputs(input, dimension):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    row_count = len(lines)
    assert len(lines[0]) == row_count

    cubes = {}
    for i in range(row_count):
        for j in range(row_count):
            coordinates = (i,j) + (0,) * (dimension-2)
            if lines[i][j] == '#':
                cubes[coordinates] = 1
    return cubes, row_count

def solve(input):
    dimension = 3
    cubes, cube_size = read_inputs(input, dimension)
    cubes_count = count_active_cubes(cubes, cube_size, iteration=6, dimension=dimension)
    print("[part 1] Active cubes after 6 cycles:", cubes_count)

def count_active_cubes(cubes, cube_size, iteration, dimension):
    z_count = 1
    neighbors_deltas = list(product((-1, 0, 1), repeat=dimension))

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
    return len(cubes)


def count_active_cubes2(cubes, cube_size, iteration, dimension):
    z_count = 1
    w_count = 1
    neighbors_deltas = list(product((-1, 0, 1), repeat=dimension))

    for _ in range(iteration):
        new_cubes = {}
        for i in range(-iteration, cube_size + iteration):
            for j in range(-iteration, cube_size + iteration):
                for z in range(-iteration, z_count + iteration):
                    for w in range(-iteration, w_count + iteration):
                        coordinate = (i, j, z, w)
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
    return len(cubes)


def solve2(input):
    dimension = 4
    cubes, cube_size = read_inputs(input, dimension)
    cubes_count = count_active_cubes2(cubes, cube_size, iteration=6, dimension=dimension)
    print("[part 2] Active cubes after 6 cycles:", cubes_count)


solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")
