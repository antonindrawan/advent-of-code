#! /usr/bin/env python3

# https://adventofcode.com/2020/day/18

import os, re
from itertools import product


def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def translate_rules(rules, idx, rule):
    if len(translated_rules[idx]) > 0:
        return translated_rules[idx]

    if rule in [['a'], ['b']]:
        return rule
    elif '|' in rule:
        tmp = []
        for indexes in rule.split('|'):
            part = translate_rules(rules, idx, indexes.strip())
            tmp.extend(part)
        translated_rules[idx] = tmp
        return tmp

    else:
        tmp = []
        for num in rule.split():
            rule_index = int(num)
            part = translate_rules(rules, rule_index, rules[rule_index])
            tmp.append(part)

        return [''.join(element) for element in product(*tmp)]


def build_regex_pattern(rule):
    pattern = '|'.join(rule)
    return '(' + pattern + ')'


def solve(input):
    rules = []
    global translated_rules
    translated_rules = []
    for i in range(150):
        rules.append('')
        translated_rules.append([])
    inputs = read_inputs(input)
    inputs_len = len(inputs)
    i = 0
    while i < inputs_len:
        line = inputs[i]
        if ':' in line:
            rule = line.split(':')

            rule_index = int(rule[0])
            rules[rule_index] = rule[1].strip()
            if '"' in rules[rule_index]:
                rules[rule_index] = [rules[rule_index][1]]
                translated_rules[rule_index] = rules[rule_index]
        else:
            break
        i += 1

    for idx, rule in enumerate(rules):
        translated_rules[idx] = translate_rules(rules, idx, rule)
        #if len(rule) > 0:
        #    print(idx, rule, translated_rules[idx])

    # Part 1
    input_start_index = i
    matches = []
    while i < inputs_len:
        #print("input: ", inputs[i])
        if inputs[i] in translated_rules[0]:
            #print(inputs[i])
            matches.append(inputs[i])
        i += 1
    print("[part 1]", len(matches))

    # Part 2
    """
    0: 8 11                 --> (42){2,} (31)+
    8: 42 | 42 8            --> (42)+
    11: 42 31 | 42 11 31    --> (42)+ (31)+
    """
    print("rule[31]", translated_rules[31])
    print("rule[42]", translated_rules[42])

    # Part 2
    # pattern: (rule 42)+((rule 42){n}(rule 31){n})
    part2_patterns = []
    regex_42 = build_regex_pattern(translated_rules[42])
    regex_31 = build_regex_pattern(translated_rules[31])

    for j in range(1, 5):
        part2_patterns.append(re.compile(regex_42 + "+" + "(" + regex_42 + "{" + str(j) + "}" + regex_31 + "{" + str(j) + "})"))

    # restore position to the beginning of the input
    i = input_start_index

    matches = []
    j = 0
    while i < inputs_len:
        #print("input: ", inputs[i])
        for pattern in part2_patterns:
            regex_matches = pattern.match(inputs[i])
            if regex_matches and regex_matches[0] == inputs[i]:
                #print(i - input_start_index, inputs[i])
                matches.append(inputs[i])
                break
        i += 1
        j += 1
    print("[part 2]", len(matches))

#solve("in_short.txt")
#solve("in_short2.txt")
solve("in.txt")

