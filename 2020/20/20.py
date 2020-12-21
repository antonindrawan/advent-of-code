#! /usr/bin/env python3

# https://adventofcode.com/2020/day/20

import math, os, re
from itertools import permutations
from functools import reduce
from copy import deepcopy

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3
REVERSED_TOP = 4
REVERSED_BOTTOM = 5
REVERSED_LEFT = 6
REVERSED_RIGHT = 7

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
            self.borders = deepcopy(self.generate_borders())
        return self.borders

    def generate_borders(self):
        size = len(self.image)
        borders = []
        # top
        borders.append(self.image[0])

        # bottom
        borders.append(self.image[size-1])

        left_border = []
        right_border = []
        for x in range(0, size):
            left_border.append(self.image[x][0])
            right_border.append(self.image[x][-1])
        borders.append(''.join(left_border))
        borders.append(''.join(right_border))
        return borders


    def get_flipped_borders(self):
        if not self.flipped_borders:
            self.flipped_borders = deepcopy(self.generate_flipped_borders())
        return self.flipped_borders


    def generate_flipped_borders(self):
        size = len(self.image)
        flipped_borders = []

        for b in self.get_borders():
            flipped_borders.append(''.join([b[x] for x in range(size-1, -1, -1)]))
        return flipped_borders

    def rotate_90(self, times=1):
        self.image = self.rotate_90_copy(times)
    def rotate_90_copy(self, times=1):
        image_cpy = deepcopy(self.image)
        for _ in range(times):
            image_cpy = [''.join(list(reversed(i))) for i in zip(*image_cpy)]
        return image_cpy

    def flip_h(self):
        self.image = self.flip_h_copy()
    def flip_h_copy(self):
        return [i for i in reversed(self.image)]

    def flip_v(self):
        self.image = self.flip_v_copy()
    def flip_v_copy(self):
        return [''.join(reversed(i[:])) for i in self.image]

    def remove_borders(self):
        size = len(self.image)
        del self.image[size-1]
        del self.image[0]

        new_image = []
        for line in self.image:
            new_image.append(line[1:size-1])
        self.image = new_image


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
    global tiles
    tiles = []

    for line in inputs:
        if line.startswith('Tile'):
            matches = re.match('Tile (\d+)', line)
            tile = Tile(int(matches[1]))
            tiles.append(tile)
            tile_counter += 1
        else:
            tiles[tile_counter-1].image.append(line)

    tiles.sort(key=lambda x: x.id)

    corner_tiles = []
    global tile_count
    tile_count = len(tiles)
    for i in range(tile_count):
        borders1 = deepcopy(tiles[i].get_borders())
        borders1.extend(tiles[i].get_flipped_borders())
        total_neighbor = 0
        for j in range(tile_count):
            if i != j:
                #print("Checking", tiles[i].id, tiles[j].id)
                borders2 = deepcopy(tiles[j].get_borders())
                borders2.extend(tiles[j].get_flipped_borders())

                count = count_matching_borders(borders1, borders2)
                assert count == 0 or count == 1
                total_neighbor += count

        # Corner tiles have exactly 2 neighbors
        if total_neighbor == 2:
            corner_tiles.append(i)
            print(f"Tile id {tiles[i].id} has neighbors {total_neighbor}")

    # part 1
    corner_tile_ids = [tiles[id].id for id in corner_tiles]
    part1_result = reduce(lambda x, y: x * y, corner_tile_ids)
    print(f"[part 1] ", part1_result)

    # Part 2
    global grid_size
    grid_size = int(math.sqrt(tile_count))

    global image_grid_dict
    image_grid_dict = dict()


    # Breadth First Search
    queue = []
    queue.append((corner_tiles[0], 0, 0))
    image_grid_dict[(0,0)] = (corner_tiles[0], tiles[corner_tiles[0]].id)
    while queue:
        (tile_index, i, j) = queue.pop(0)
        print("Processing", tiles[tile_index].id, i, j)
        for n, row, col in neighbors(tile_index, i, j):
            print("Adding neighbor", tiles[n].id, row, col)
            queue.append((n, row, col))

    # Ensure the grid is populated with all avalable tile ids.
    assert len(set([tile.id for tile in tiles]) - set([tile_id for tile_idx, tile_id in image_grid_dict.values()])) == 0

    # Remove borders
    for tile in tiles:
        tile.remove_borders()
    print_grid_dict()

    # Combine into an image
    big_image = Tile(999)
    big_image.image = combine_grid()

    total_hash = sum([i.count('#') for i in big_image.image])
    print("Total #:", total_hash)

    #SEA_MONSTERS=[]
    #SEA_MONSTERS.append("                  # ")
    #SEA_MONSTERS.append("#    ##    ##    ###")
    #SEA_MONSTERS.append(" #  #  #  #  #  #   ")
    SEA_MONSTERS_COST = 15
    for i in range(2):
        tile_aux = None
        if i == 0:
            tile_aux = deepcopy(big_image)
        else:
            tile_aux = deepcopy(big_image)
            tile_aux.flip_v()
        for _ in range(1, 4): # 1-3
            tile_aux.rotate_90()
            sea_monster_count = find_sea_monster_count(tile_aux.image)
            if sea_monster_count > 0:
                print(tile_aux)
                print("[part 2]", total_hash - (sea_monster_count*SEA_MONSTERS_COST))
                break


def find_sea_monster_count(image):
    image_width = len(image)

    monsters_count = 0
    for row in range(image_width-3+1):
        row_image = image[row]
        for col in range(image_width-20+1):
            pos = col + 18
            if row_image[pos] == '#':
                #then check next row
                if (image[row+1][pos] == '#' and image[row+1][pos-1] == '#' and  image[row+1][pos+1] == '#' and
                    image[row+1][pos-6] == '#' and image[row+1][pos-7] == '#' and
                    image[row+1][pos-12] == '#' and image[row+1][pos-13] == '#' and
                    image[row+1][pos-18] == '#' and
                    image[row+2][pos-2] == '#' and image[row+2][pos-5] == '#' and image[row+2][pos-8] == '#' and image[row+2][pos-11] == '#' and
                    image[row+2][pos-14] == '#' and image[row+2][pos-17] == '#'):
                    print("Found sea monster at ", row, col)
                    monsters_count += 1

    return monsters_count


def combine_grid():
    image = []
    min_row = min([i for i, j in image_grid_dict])
    max_row= max([i for i, j in image_grid_dict])
    min_col = min([j for i, j in image_grid_dict])
    max_col = max([j for i, j in image_grid_dict])

    row_count = len(tiles[0].image)

    for i in range(min_row,max_row+1):
        for row in range(row_count):
            row_image = ""
            for j in range(min_col, max_col+1):
                tile_idx = image_grid_dict[(i, j)][0]

                row_image += tiles[tile_idx].image[row]
            image.append(row_image)
    return image

def print_grid_dict():
    print("DICT")
    min_row = min([i for i, j in image_grid_dict])
    max_row= max([i for i, j in image_grid_dict])
    min_col = min([j for i, j in image_grid_dict])
    max_col = max([j for i, j in image_grid_dict])

    for i in range(min_row,max_row+1):
        for j in range(min_col, max_col+1):
            if (i, j) in image_grid_dict:
                print(image_grid_dict[(i, j)], end='')
            else:
                print("<0, 0>", end='')
        print()
    print()


def neighbors(tile_index, grid_row, grid_col):
    neighbor_list = []
    borders1 = deepcopy(tiles[tile_index].generate_borders())
    borders1.extend(tiles[tile_index].generate_flipped_borders())
    for j in range(tile_count):
        if tile_index != j:
            borders2 = deepcopy(tiles[j].generate_borders())
            borders2.extend(tiles[j].generate_flipped_borders())

            for idx, border in enumerate(borders1):
                for idx2, border2 in enumerate(borders2):
                    if border == border2:
                        #print("->", idx, idx2, tiles[tile_index].id, tiles[j].id)
                        next_row = None
                        next_col = None
                        if idx == RIGHT:
                            next_row = grid_row
                            next_col = grid_col+1
                            if abs(next_col) > (grid_size - 1):
                                next_col = grid_col - 1

                        elif idx == LEFT:
                            next_row = grid_row
                            next_col = grid_col-1
                            if abs(next_col) > (grid_size - 1):
                                next_col = grid_col + 1
                        elif idx == TOP:
                            next_row = grid_row-1
                            next_col = grid_col
                            if abs(next_row) > (grid_size - 1):
                                next_row = grid_row + 1
                        elif idx == BOTTOM:
                            next_row = grid_row+1
                            next_col = grid_col
                            if abs(next_row) > (grid_size - 1):
                                next_row = grid_row - 1
                        else:
                            continue


                        if (next_row, next_col) != (None, None) and (next_row, next_col) not in image_grid_dict and tiles[j].id not in [item[1] for item in image_grid_dict.values()]:
                            if idx == RIGHT:
                                if idx2 == TOP:
                                    tiles[j].flip_v()
                                    tiles[j].rotate_90(times=3)
                                elif idx2 == REVERSED_TOP:
                                    tiles[j].rotate_90(times=3)
                                elif idx2 == BOTTOM:
                                    tiles[j].rotate_90()
                                elif idx2 == REVERSED_BOTTOM:
                                    tiles[j].flip_v()
                                    tiles[j].rotate_90(times=1)
                                #elif LEFT (no change)
                                elif idx2 == REVERSED_LEFT:
                                    tiles[j].flip_h()
                                elif idx2 == RIGHT:
                                    tiles[j].flip_v()
                                elif idx2 == REVERSED_RIGHT:
                                    tiles[j].flip_h()
                                    tiles[j].flip_v()
                            elif idx == LEFT:
                                if idx2 == TOP:
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == REVERSED_TOP:
                                    tiles[j].flip_v()
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == BOTTOM:
                                    tiles[j].flip_h()
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == REVERSED_BOTTOM:
                                    tiles[j].rotate_90(times=3)
                                elif idx2 == LEFT:
                                    tiles[j].flip_v()
                                elif idx2 == REVERSED_LEFT:
                                    tiles[j].flip_h()
                                    tiles[j].flip_v()
                                #elif idx2 == RIGHT (no change)
                                elif idx2 == REVERSED_RIGHT:
                                    tiles[j].flip_h()

                            elif idx == TOP:
                                if idx2 == TOP:
                                    tiles[j].flip_h()
                                elif idx2 == REVERSED_TOP:
                                    tiles[j].flip_h()
                                    tiles[j].flip_v()
                                #elif BOTTOM (no change)
                                elif idx2 == REVERSED_BOTTOM:
                                    tiles[j].flip_v()
                                elif idx2 == LEFT:
                                    tiles[j].rotate_90(times=3)
                                elif idx2 == REVERSED_LEFT:
                                    tiles[j].flip_v()
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == RIGHT:
                                    tiles[j].rotate_90(times=1)
                                    tiles[j].flip_v()
                                elif idx2 == REVERSED_RIGHT:
                                    tiles[j].rotate_90(times=1)

                            elif idx == BOTTOM:
                                # if idx2 == TOP: (no change)
                                if idx2 == REVERSED_TOP:
                                    tiles[j].flip_v()
                                elif idx2 == BOTTOM:
                                    tiles[j].flip_h()
                                elif idx2 == REVERSED_BOTTOM:
                                    tiles[j].flip_h()
                                    tiles[j].flip_v()
                                elif idx2 == LEFT:
                                    tiles[j].flip_h()
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == REVERSED_LEFT:
                                    tiles[j].rotate_90(times=1)
                                elif idx2 == RIGHT:
                                    tiles[j].rotate_90(times=3)
                                elif idx2 == REVERSED_RIGHT:
                                    tiles[j].flip_v()
                                    tiles[j].rotate_90(times=1)

                            image_grid_dict[(next_row, next_col)] = (j, tiles[j].id)
                            neighbor_list.append((j, next_row, next_col))
    return neighbor_list


#solve("in_short.txt")
solve("in.txt")
