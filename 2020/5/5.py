#! /usr/bin/env python3

ROW_COUNT = 128 # 0-127
COL_COUNT = 8   # 0-7

def get_boarding_passes(input_file):
    boarding_passes = []
    with open(input_file, "r") as f:
        boarding_passes = (line.strip() for line in f.readlines())
    return boarding_passes


def get_seat(boarding_pass):

    row = 0
    row_range = (0, ROW_COUNT-1)
    diff = ROW_COUNT
    for i in range(0, 7):
        if boarding_pass[i] == 'B':
            row_range = (row_range[0] + (diff // 2), row_range[1])
        elif boarding_pass[i] == 'F':
            row_range = (row_range[0], row_range[1] - (diff // 2))
        diff /= 2

    row = int(row_range[0]) # or row_range[1] does not matter

    col_range = (0, COL_COUNT-1)
    diff = COL_COUNT
    for i in range(7, 10):
        if boarding_pass[i] == 'L':
            col_range = (col_range[0], col_range[1] - (diff // 2))
        elif boarding_pass[i] == 'R':
            col_range = (col_range[0] + (diff // 2), col_range[1])
        diff /= 2
    col = int(col_range[0])

    seat_id = row * 8 + col
    return row, col, seat_id


def get_seat_ids(input_file):
    seat_ids = []
    for i in get_boarding_passes(input_file):
        _, _, seat_id = get_seat(i)
        seat_ids.append(seat_id)
    return seat_ids


def solve1(input_file):
    seat_ids = get_seat_ids(input_file)
    print(f"[part 1] The max seat ID is {max(seat_ids)}")


def solve2(input_file):
    seat_ids = get_seat_ids(input_file)

    # The next seat id is always +1 from the current seat id.
    #   If it starts with 8, then the next ones are 9, 10, 11, and so on.
    # The available one is where you detect the next occupied seat id is not +1  from the current seat ID (i.e. +2).
    #   e.g. 20, 21, 23, 24, ... -> then the available seat ID is 22
    sorted_seat_ids = sorted(seat_ids)
    for i in sorted_seat_ids:
        if sorted_seat_ids[i] + 1 != sorted_seat_ids[i+1]:
            print(f"[part 2] The available seat ID is {sorted_seat_ids[i] + 1}")
            break

solve1("in.txt")
solve2("in.txt")