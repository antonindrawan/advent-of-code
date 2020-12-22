#! /usr/bin/env python3

# https://adventofcode.com/2020/day/22

import os
from copy import deepcopy

def read_inputs(input):
    lines = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, input), "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    card_decks = []
    card_decks.append([])
    card_decks.append([])
    player_idx = -1
    for line in lines:
        if "Player" in line:
            player_idx += 1
        else:
            card_decks[player_idx].append(int(line))

    return card_decks


def solve(input):
    card_decks = read_inputs(input)

    while card_decks[0] and card_decks[1]:
        a = card_decks[0].pop(0)
        b = card_decks[1].pop(0)
        if a < b:
            card_decks[1].append(b)
            card_decks[1].append(a)
        else:
            card_decks[0].append(a)
            card_decks[0].append(b)

    winner = 0
    if card_decks[1]:
        winner = 1

    card_count = len(card_decks[winner])
    result = sum([card_decks[winner].pop(0) * i for i in range(card_count, 0, -1)])
    print("[Part 1]", result)


def start_game(card_decks, round):
    winner = -1
    card_decks_history = []
    while card_decks[0] and card_decks[1]:
        if card_decks in card_decks_history:
            winner = 0 # player 1 wins
            # print(f"[STOP] Player 1 wins, because both players' card decks are the same as the input to prevent an infinite game")
            return winner

        card_decks_history.append(deepcopy(card_decks))

        a = card_decks[0].pop(0)
        b = card_decks[1].pop(0)
        if a <= len(card_decks[0]) and b <= len(card_decks[1]):
            #print(f"Start mini game at round {round}")

            sub_game_card_decks = []
            sub_game_card_decks.append(card_decks[0][:a])
            sub_game_card_decks.append(card_decks[1][:b])
            winner = start_game(sub_game_card_decks, 1)
            #print(f"End of mini game at round {round}")

            if winner == 1:
                card_decks[1].append(b)
                card_decks[1].append(a)
            else:
                card_decks[0].append(a)
                card_decks[0].append(b)
        else:
            if a < b: # player2 wins
                card_decks[1].append(b)
                card_decks[1].append(a)
            else: # player 1 wins
                card_decks[0].append(a)
                card_decks[0].append(b)
        round += 1

    if card_decks[0]:
        winner = 0
    elif card_decks[1]:
        winner = 1

    return winner


def solve2(input):
    card_decks = read_inputs(input)

    winner = start_game(card_decks, 1)
    card_count = len(card_decks[winner])
    result = sum([card_decks[winner].pop(0) * i for i in range(card_count, 0, -1)])
    print("[Part 2]", result)

solve("in_short.txt")
solve("in.txt")
solve2("in_short.txt")
solve2("in_short2.txt")
solve2("in.txt")

# pypy 22.py  88,81s user 0,06s system 99% cpu 1:28,89 total
