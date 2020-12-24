#! /usr/bin/env python3

# https://adventofcode.com/2020/day/24

import os, re
from copy import deepcopy
import operator

HEXAGON_PATTERN = re.compile("(e|se|sw|w|nw|ne)")

EAST = (0,  2)
SOUTH_EAST = (-1,  1)
SOUTH_WEST = (-1, -1)
WEST = ( 0, -2)
NORTH_WEST = ( 1, -1)
NORTH_EAST = ( 1,  1)
NEIGHBOR_DELTAS = [EAST, SOUTH_EAST, SOUTH_WEST, WEST, NORTH_WEST, NORTH_EAST]

# Black tiles are odd numbers, white tiles are even numbers

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def neighbors(tiles, tile):
    black_tile_neighbors = []
    white_tile_neighbors = []
    for neighbor_delta in NEIGHBOR_DELTAS:
        neighbor = tuple(map(operator.add, tile, neighbor_delta))
        if neighbor in tiles and tiles[neighbor] % 2 == 1:
            black_tile_neighbors.append(neighbor)
        else:
            white_tile_neighbors.append(neighbor)

    return black_tile_neighbors, white_tile_neighbors


def solve(input):
    visited_tiles = {}
    for line in read_inputs(input):
        pos = (0, 0)
        matches = HEXAGON_PATTERN.findall(line)
        for dir in matches:
            if dir == 'e':
                pos = tuple(map(operator.add, pos, EAST))
            elif dir == 'se':
                pos = tuple(map(operator.add, pos, SOUTH_EAST))
            elif dir == 'sw':
                pos = tuple(map(operator.add, pos, SOUTH_WEST))
            elif dir == 'w':
                pos = tuple(map(operator.add, pos, WEST))
            elif dir == 'nw':
                pos = tuple(map(operator.add, pos, NORTH_WEST))
            elif dir == 'ne':
                pos = tuple(map(operator.add, pos, NORTH_EAST))
        if pos not in visited_tiles:
            visited_tiles[pos] = 1
        else:
            visited_tiles[pos] += 1

    black_tiles = [tile for tile, visited_count in visited_tiles.items() if visited_count % 2 == 1]
    print(f"[part 1] black_tiles_count: {len(black_tiles)}")

    # part 2
    for _ in range(100):
        checked_white_tiles = {}

        mark_as_white = {}
        mark_as_black = {}
        for black_tile in black_tiles:
            black_tile_neighbors, white_tiles_neighbors = neighbors(visited_tiles, black_tile)
            black_tile_neighbors_count = len(black_tile_neighbors)
            if black_tile_neighbors_count == 0 or black_tile_neighbors_count > 2:
                mark_as_white[black_tile] = 1 # becomes white


            for white_tile in white_tiles_neighbors:
                if white_tile not in checked_white_tiles:
                    checked_white_tiles[white_tile] = 1
                    blacks, _ = neighbors(visited_tiles, white_tile)
                    if len(blacks) == 2:
                        mark_as_black[white_tile] = 1
                else:
                    # skip it
                    pass
            pass

        for tile in mark_as_black:
            visited_tiles[tile] = 1
        for tile in mark_as_white:
            visited_tiles[tile] = 0
        black_tiles = [tile for tile, visited_count in visited_tiles.items() if visited_count % 2 == 1]
    black_tiles = [tile for tile, visited_count in visited_tiles.items() if visited_count % 2 == 1]
    print(f"[part 2] black_tiles_count: {len(black_tiles)}")

solve("in_short.txt")
solve("in.txt")