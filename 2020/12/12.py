#! /usr/bin/env python3

# https://adventofcode.com/2020/day/12

import os

from itertools import combinations
from copy import deepcopy
from collections import Counter

# North, East, South, West
NESW_DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
NESW_DIRECTIONS_MAP = {'N': 0, 'E': 1, 'S': 2, 'W': 3}


def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def rotate_direction(direction, degrees):
    rotate_index = int(degrees / 90)
    current_index = NESW_DIRECTIONS.index(direction)

    new_index = (rotate_index + current_index) % 4
    return NESW_DIRECTIONS[new_index]

pos = (0, 0)

def solve(input):
    pos = (0, 0)
    direction = (0, 1) # heading east
    for i in read_inputs(input):
        action = i[:1]
        count = int(i[1:])

        if action == 'F':
            pos = tuple(map(lambda x, y: x + y, pos, (direction[0] * count, direction[1] * count)))
        elif action in 'NSEW':
            movement = NESW_DIRECTIONS[NESW_DIRECTIONS_MAP[action]]
            pos = tuple(map(lambda x, y: x + y, pos, (movement[0] * count, movement[1] * count)))
        elif action == 'L':
            direction = rotate_direction(direction, -count)
        elif action == 'R':
            direction = rotate_direction(direction, count)
        #print(f" -> pos: {pos}, direction: {direction}")

    print("[part 1] The sum of the absolute values of its position", abs(pos[0]) + abs(pos[1]))


def rotate_waypoint(waypoint, degrees):
    #e.g. every 90 deg clockwise rotation: 4,10 -> -10,4 -> -4,-10 -> 10,-4
    rotate_index = int(degrees / 90) % 4
    for _ in range(rotate_index):
        waypoint = (-waypoint[1], waypoint[0])

    return waypoint

def solve2(input):
    pos = (0, 0)
    waypoint = (1, 10)
    for i in read_inputs(input):
        action = i[:1]
        count = int(i[1:])

        if action == 'F':
            movement = (waypoint[0] * count, waypoint[1] * count)
            pos = tuple(map(lambda x, y: x + y, pos, movement))
        elif action in 'NSEW':
            movement = NESW_DIRECTIONS[NESW_DIRECTIONS_MAP[action]]
            waypoint = tuple(map(lambda x, y: x + y, waypoint, (movement[0] * count, movement[1] * count)))
        elif action == 'L':
            waypoint = rotate_waypoint(waypoint, -count)
        elif action == 'R':
            waypoint = rotate_waypoint(waypoint, count)
        #print(f" -> pos: {pos}, waypoint: {waypoint}")
    print("[part 2] The sum of the absolute values of its position", abs(pos[0]) + abs(pos[1]))

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")