#! /usr/bin/env python3

# https://adventofcode.com/2020/day/18

import os, re
from itertools import product
import operator

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip().replace(" ", "") for line in f.readlines() if line.strip()]
    return lines


def calculate(line):
    operator = None
    result = 0
    length = len(line)
    i = 0
    while i < length:
        char = line[i]
        if char in ['+', '*']:
            operator = char
        elif char == '(':
            number, consumed = calculate(line[i+1:])
            i += consumed
            if not operator:
                result += number
            elif operator == '+':
                result += number
            elif operator == '*':
                result *= number
        elif char == ')':
            i += 1
            break
        elif char >= '0' and char <='9':
            number = int(char)
            if not operator:
                result = number
            elif operator == '+':
                result += number
            elif operator == '*':
                result *= number
            #print(number, result)
        i += 1
    return result, i


def solve(input):
    results = []
    for line in read_inputs(input):
        result, consumed = calculate(line)
        #print(result, consumed, len(line))
        results.append(result)
    print("[part 1] Sum of resulting values: ", sum(results))


def add_parentheses_for_addition(line):
    """
    Input: ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
    Output:

    Recursive:
    a = (2 + 4 * (9))    --> ((2 + 4 * (9))) * ((6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
    b = (6 + 9 * 8 + 6)  --> ((2 + 4 * (9)) * ((6 + 9 * (8 + 6)) + 6)) + 2 + 4 * (2)
    c = (a * b + 6)
    c + 2 + 4 * 2
    """

    i = 0
    queue = []
    while i < len(line):
        char = line[i]
        if char == '(':
            altered, consumed = add_parentheses_for_addition(line[i+1:])
            line = line[:i+1] + altered
            i += consumed
        elif char == ')':
            if len(queue) > 0:
                assert len(queue) == 1
                queue.pop()
                line = line[:i] + ')' + line[i:]
                i += 1 # because we insert a ')', so the position of * is shifted
            i += 1
            break
        elif char == '*':
            if len(queue) > 0:
                assert len(queue) == 1
                queue.pop()
                line = line[:i] + ')' + line[i:]
                i += 1 # because we insert a ')', so the position of * is shifted

            line = line[:i+1] + '(' + line[i+1:]
            queue.append('(')
            i += 1
        i += 1
    if len(queue) > 0:
        assert len(queue) == 1
        queue.pop()
        line = line[:i] + ')' + line[i:] # eq. line += ')'
        i += 1
    return line, i

def solve2(input):
    results = []
    for line in read_inputs(input):
        line, _ = add_parentheses_for_addition(line)
        result, consumed = calculate(line)
        #print(line, "result =", result, ". Consumed vs len = ", consumed, len(line))
        results.append(result)
    print("[part 2] Sum of resulting values: ", sum(results))

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in.txt")
