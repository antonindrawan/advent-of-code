#! /usr/bin/env python3

# https://adventofcode.com/2020/day/16

import os, re, sys
from itertools import permutations

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


RULE = re.compile("^(.+): (\d+)-(\d+) or (\d+)-(\d+)")

def read(input):
    my_ticket = []
    nearby_tickets = []
    rules = dict()

    for line in read_inputs(input):
        matches = RULE.match(line)
        if matches:
            rules[matches[1]] = [int(matches[2]), int(matches[3]), int(matches[4]), int(matches[5])]
        elif "your ticket" in line:
            read_my_ticket = True
        elif "nearby tickets" in line:
            read_my_ticket = False
        else:
            if read_my_ticket:
                my_ticket = [int(val) for val in line.split(',')]
            else:
                ticket = [int(val) for val in line.split(',')]
                nearby_tickets.append(ticket)

    #print(rules)
    #print(my_ticket)
    #for ticket in nearby_tickets:
    #    print(ticket)
    return rules, my_ticket, nearby_tickets


def solve(input):
    rules, _, nearby_tickets = read(input)
    # Part 1
    all_numbers = set()
    for _, values in rules.items():
        tmp = [x for x in range(values[0], values[1] + 1)]
        tmp.extend([x for x in range(values[2], values[3] + 1)])
        for val in tmp:
            all_numbers.add(val)

    answer = []
    for ticket in nearby_tickets:
        answer.extend([i for i in ticket if i not in all_numbers])

    print("[part 1]", sum(answer))


def recurse2(nearby_tickets, ticket_idx, rules_names, rules_length):
    if ticket_idx == rules_length:
        return True

    for rule_idx in range(rules_length):
        if rule_idx not in valid_indexes:
            rule_idx_valid = True
            for ticket in nearby_tickets:
                el = ticket[ticket_idx]
                if not ((el >= rules_names[rule_idx][1][0] and el <= rules_names[rule_idx][1][1]) or (el >= rules_names[rule_idx][1][2] and el <= rules_names[rule_idx][1][3])):
                    rule_idx_valid = False
                    break

            if rule_idx_valid:
                valid_indexes.append(rule_idx)
                if recurse2(nearby_tickets, ticket_idx + 1, rules_names, rules_length):
                    return True
                # restore the state
                valid_indexes.pop()


    return False

def solve2(input):
    rules, my_ticket, nearby_tickets = read(input)
    # Part 1
    all_numbers = set()
    for _, values in rules.items():
        tmp = [x for x in range(values[0], values[1] + 1)]
        tmp.extend([x for x in range(values[2], values[3] + 1)])
        for val in tmp:
            all_numbers.add(val)

    rules_names = list(rules.items())
    nearby_tickets[:] = [ticket for ticket in nearby_tickets if all(i in all_numbers for i in ticket)]

    global available_indexes
    available_indexes = list(range(len(rules)))

    global valid_indexes
    valid_indexes = []
    ticket_idx = 0
    found = recurse2(nearby_tickets, ticket_idx, rules_names, len(rules_names))
    if found:
        print(valid_indexes)

        print(my_ticket)
        if len(valid_indexes) > 6:
            result = 1
            for i in range(0, 6):
                result *= my_ticket[valid_indexes.index(i)]
            print("[part 2]", result)
    else:
        print("[part 2] not found")


solve("in_short.txt")
solve("in.txt")
#solve2("in_short2.txt")
solve2("in.txt")