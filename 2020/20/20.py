#! /usr/bin/env python3

# https://adventofcode.com/2020/day/18

import math, os, re
from itertools import permutations
from functools import reduce

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

class Tile:
    def __init__(self, id):
        self.id = id
        self.image = []
        self.borders = None
        self.flipped_borders = None

    def __repr__(self):
        output = f"Tile: {self.id}"
        output += "\n"

        for i in self.image:
            output += i + "\n"
        return output


    def get_borders(self):
        if not self.borders:
            size = len(self.image)
            self.borders = []
            self.borders.append(self.image[0])
            self.borders.append(self.image[size-1])

            left_border = []
            right_border = []
            for x in range(0, size):
                left_border.append(self.image[x][0])
                right_border.append(self.image[x][-1])
            self.borders.append(''.join(left_border))
            self.borders.append(''.join(right_border))

        return self.borders

    def get_flipped_borders(self):
        if not self.flipped_borders:
            size = len(self.image)
            self.flipped_borders = []
            borders = self.get_borders()
            for b in borders:

                self.flipped_borders.append(''.join([b[x] for x in range(size-1, -1, -1)]))
        return self.flipped_borders

def count_matching_borders(borders1, borders2):
    count = 0
    for b1 in borders1:
        if b1 in borders2:
            count += 1
            break
    return count

def solve(input):
    inputs = read_inputs(input)
    tile_counter = 0
    tiles = []
    for line in inputs:
        if line.startswith('Tile'):
            matches = re.match('Tile (\d+)', line)
            tile = Tile(int(matches[1]))
            tiles.append(tile)
            tile_counter += 1
        else:
            tiles[tile_counter-1].image.append(line)

    corner_tiles = []
    tile_count = len(tiles)
    for i in range(tile_count):
        borders1 = tiles[i].get_borders()
        borders1.extend(tiles[i].get_flipped_borders())
        total_neighbor = 0
        for j in range(tile_count):
            if i != j:
                #print("Checking", tiles[i].id, tiles[j].id)
                borders2 = tiles[j].get_borders()
                borders2.extend(tiles[j].get_flipped_borders())

                count = count_matching_borders(borders1, borders2)
                if count > 0:
                    total_neighbor += 1

        # Corner tiles have exactly 2 neighbors
        if total_neighbor == 2:
            corner_tiles.append(tiles[i].id)
            print(f"Tile id {tiles[i].id} has 2 neighbors {total_neighbor}")

    print(f"[part 1] ", reduce(lambda x, y: x * y, corner_tiles))
solve("in_short.txt")
solve("in.txt")