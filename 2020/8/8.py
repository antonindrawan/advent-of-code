import copy
import os
import re

INSTR_PATTERN = re.compile("^(.+) ([+-])([0-9]+)")

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def read_instructions(input):
    instructions = []
    for line in read_inputs(input):
        matches = INSTR_PATTERN.match(line)
        if matches:
            visited = False
            op = matches[1]
            step = int(matches[3])
            if  matches[2] == "-":
                step = -step
            ins = [visited, op, step]
            instructions.append(ins)

    return instructions

def sol(instructions):
    accumulator = 0
    n = len(instructions)
    i = 0
    while i < n and not instructions[i][0]:
        if instructions[i][1] == "acc":
            instructions[i][0] = True
            accumulator += instructions[i][2]
            i += 1
        elif instructions[i][1] == "jmp":
            instructions[i][0] = True
            i += instructions[i][2]
        elif instructions[i][1] == "nop":
            instructions[i][0] = True
            i += 1

    return i, accumulator


def solve1(input):
    instructions = read_instructions(input)
    _, accumulator = sol(instructions)
    print(f"[part 1] Accumulator is {accumulator}")

def solve2(input):
    instructions = read_instructions(input)
    n = len(instructions)

    swap_op = ['nop', 'jmp']

    accumulator = 0
    for i in range(0, n):
        op = instructions[i][1]
        if op in swap_op:
            index = swap_op.index(op)
            index = (index + 1) % 2

            instructions_cpy = copy.deepcopy(instructions)
            instructions_cpy[i][1] = swap_op[index]
            index, accumulator = sol(instructions_cpy)
            if index >= n:
                break

    print(f"[part 2] Accumulator is {accumulator}")

solve1("in_short.txt")
solve1("in.txt")
solve2("in_short.txt")
solve2("in.txt")