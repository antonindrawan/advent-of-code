#! /usr/bin/env python3

# https://adventofcode.com/2020/day/11

import os

from itertools import combinations
from copy import deepcopy
from collections import Counter

ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

class Seat:
    def __init__(self, current):
        self.current = current
        self.row = len(current)
        self.col = len(current[0])

    def should_become_occupied(self, current, i, j):
        assert current[i][j] == 'L'

        for dx, dy in ADJACENTS:
            x = j + dx
            y = i + dy
            if y < 0 or y >= self.row or x < 0 or x >= self.col:
                continue

            if current[y][x] == '#':
                return False
        return True


    def should_become_empty(self, current, i, j):
        assert current[i][j] == '#'

        count = 0
        for dx, dy in ADJACENTS:
            x = j + dx
            y = i + dy
            if y < 0 or y >= self.row or x < 0 or x >= self.col:
                continue

            if current[y][x] == '#':
                count += 1
        if count >= 4:
            return True
        return False


    def apply_rules(self):
        """
        return next after applying rules:

        The following rules are applied to every seat simultaneously:

        If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.
        """

        next = deepcopy(self.current)

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.current[i][j] == 'L' and self.should_become_occupied(self.current, i, j):
                    next[i][j] = '#'
                elif self.current[i][j] == '#' and self.should_become_empty(self.current, i, j):
                    next[i][j] = 'L'

        return next


    def should_become_occupied2(self, current, i, j):
        assert current[i][j] == 'L'

        for dx, dy in ADJACENTS:

            x = j + dx
            y = i + dy
            while not (y < 0 or y >= self.row or x < 0 or x >= self.col):

                if current[y][x] == '#': # TODO, return true if L is found
                    return False
                elif current[y][x] == 'L':
                    break
                x += dx
                y += dy
        return True


    def should_become_empty2(self, current, i, j):
        assert current[i][j] == '#'

        count = 0
        for dx, dy in ADJACENTS:
            x = j + dx
            y = i + dy
            while not (y < 0 or y >= self.row or x < 0 or x >= self.col):

                if current[y][x] == '#':
                    count += 1
                    break
                elif current[y][x] == 'L':
                    break
                x += dx
                y += dy


        if count >= 5:
            return True
        return False


    def apply_rules2(self):
        """
        all directions

        If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        If a seat is occupied (#) and FIVE or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.
        """

        next = deepcopy(self.current)

        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.current[i][j] == 'L' and self.should_become_occupied2(self.current, i, j):
                    next[i][j] = '#'
                elif self.current[i][j] == '#' and self.should_become_empty2(self.current, i, j):
                    next[i][j] = 'L'

        return next

def solve(input):
    """
    # = occupied
    L = empty
    . = floor
    """

    input = read_inputs(input)
    next = []
    for i in input:
        next.append(list(i))

    current = None
    while current != next:
        current = next
        seat = Seat(current)
        next = seat.apply_rules()

    print("[part 1] The number of occupied seats is", sum(i.count('#') for i in next))


def solve2(input):
    input = read_inputs(input)
    next = []
    for i in input:
        next.append(list(i))

    current = None
    while current != next:
        current = next
        seat = Seat(current)
        next = seat.apply_rules2()

    print("[part 2] The number of occupied seats is", sum(i.count('#') for i in next))

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")
