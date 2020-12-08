#! /usr/bin/env python3

import re
import sys

"""
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

"""

mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def valid_passport(filled_keys):
    valid = True

    for key in mandatory_keys:
        if key not in filled_keys:
            valid = False
            break
    return valid


def solve(part):
    filled_keys = []
    valid_passport_count = 0
    with open("in.txt", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    for line in lines:
        if not line:
            if valid_passport(filled_keys):
                valid_passport_count += 1

            # print("New case")
            filled_keys = []
        else:
            pairs = line.split()

            for pair in pairs:
                key, val = pair.split(":")

                if (part == "2"):
                    valid = True
                    if key == "byr":
                        byr = int(val)
                        valid = (byr >= 1920 and byr <= 2002)

                    elif key == "iyr":
                        iyr = int(val)
                        valid = (iyr >= 2010 and iyr <= 2020)

                    elif key == "eyr":
                        eyr = int(val)
                        valid = (eyr >= 2020 and eyr <= 2030)

                    elif key == "hgt":
                        valid = "cm" in val or "in" in val
                        if valid:
                            try:
                                height = int(val[:-2])
                                height_unit = val[-2:]
                                if height_unit == "cm":
                                    valid = (height >= 150 and height <= 193)
                                elif height_unit == "in":
                                    valid = (height >= 59 and height <= 76)
                            except ValueError:
                                valid = False

                    elif key == "hcl":
                        valid = len(val) == 7 and re.search("#[0-9a-f]*", val)

                    elif key == "ecl":
                        valid = val in ["amb", "blu", "brn", "gry" ,"grn", "hzl", "oth"]

                    elif key == "pid":
                        valid = re.search("^[0-9]{9}$", val)

                    if valid:
                        filled_keys.append(key)

                else:
                    filled_keys.append(key)

    if valid_passport(filled_keys):
        valid_passport_count += 1
    return valid_passport_count

if __name__ == "__main__":
    print(f"[part 1] Total valid password: {solve('1')}")
    print(f"[part 2] Total valid password: {solve('2')}")
