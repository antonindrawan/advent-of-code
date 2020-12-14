#! /usr/bin/env python3

# https://adventofcode.com/2020/day/13

import os

from itertools import combinations
from copy import deepcopy
from collections import Counter

def read_inputs(input):
    times = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        departure_time = int(f.readline())
        times = f.readline().split(',')
    return departure_time, times


def solve(input):
    departure_time, times = read_inputs(input)

    valid_times = list(filter(lambda time: time != 'x', times))
    valid_times = [int(time) for time in valid_times]

    print(departure_time, times, valid_times)
    closest_departure_time = departure_time
    closest_bus_id = 0
    found = False
    while (True):
        for time in valid_times:
            if closest_departure_time % time == 0:
                print(closest_departure_time, time)
                closest_bus_id = time
                found = True
                break
        if found:
            break
        closest_departure_time += 1
    print(f"[part 1] {(closest_departure_time - departure_time) * closest_bus_id}")


def solve2(input):
    valid_times = []
    departure_time, times = read_inputs(input)
    i = 0
    for time in times:
        if time != 'x':
            int_time = int(time)
            valid_times.append((i, int_time))

        i += 1
    valid_times = sorted(valid_times, key=lambda tup: tup[1])
    for i in valid_times:
        print(i)

    n = len(valid_times)
    smallest = valid_times[0]
    highest = valid_times[n-1]
    print("Smallest", smallest)
    print("Highest", highest)
    for bus in valid_times:
        print(bus)

    timestamp = 1
    step = 1
    for bus in valid_times:
        while (timestamp + bus[0]) % bus[1] != 0:
            timestamp += step
            #print(timestamp)

        # I think this should ideally be a least common multiple (lcm), but since the all inputs are prime numbers, the lcm is the product of numbers.
        step *= bus[1]
        #print("step, timestamp ", step, timestamp)
    print("[part 2] ", timestamp)

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")