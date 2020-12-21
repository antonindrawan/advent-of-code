#! /usr/bin/env python3

# https://adventofcode.com/2020/day/21

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

def get_ingredient_allergent_map(foods):
    possibilities = dict()
    for ingredients, allergents in foods:
        for allergent in allergents:
            if allergent in possibilities:
                # only take the common ingredients, so use the & operator
                possibilities[allergent] &= set(ingredients)
            else:
                possibilities[allergent] = set(ingredients)

    ingredient_allergent = dict()
    while len(ingredient_allergent) < len(possibilities):
        matched = [allergen for allergen, ingredients in possibilities.items() if len(ingredients) == 1]
        for allergen in matched:
            ingredient = possibilities[allergen].pop()
            ingredient_allergent[ingredient] = allergen
            for ingredients in possibilities.values():
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
    return ingredient_allergent

def solve1(ingredient_allergent, foods):
    not_in_allergens = 0
    for ingredients, _ in foods:
        not_in_allergens += sum(ingredient not in ingredient_allergent for ingredient in ingredients)
    return not_in_allergens

def solve2(ingredient_allergent):
    sorted_ingredient_allergent_by_allergent = sorted(ingredient_allergent.items(), key=lambda x : x[1])
    return ','.join([x[0] for x in sorted_ingredient_allergent_by_allergent])

def solve(input):
    foods = []
    for i in read_inputs(input):
        input = i.replace(")", "").split("(contains ")
        ingredients = input[0].split()
        allergents = input[1].split(', ')

        print(ingredients, allergents)
        foods.append((ingredients, allergents))

    ingredient_allergent_map = get_ingredient_allergent_map(foods)
    print(ingredient_allergent_map)

    print("[part 1]", solve1(ingredient_allergent_map, foods))
    print("[part 2]", solve2(ingredient_allergent_map))

#solve("in_short.txt")
solve("in.txt")