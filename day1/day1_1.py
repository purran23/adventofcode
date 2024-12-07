#!/usr/bin/env python3
"""AOC 2024 day1"""

import re

with open("input.txt", "r", encoding="utf-8") as in_data:
    in_data = in_data.read()
in_data_list = re.split(r'["   "\n]+', in_data)


first_list = list(in_data_list[::2])
second_list = list(in_data_list[1::2])

first_list.remove("")


def part1(first: list, second: list) -> int:
    """Part 1 solution"""
    result = 0
    for f, s in zip(sorted(first), sorted(second)):
        result += abs(int(f) - int(s))

    print(f"first part: {result}")

def part2 (first: list, second: list) -> int:
    """Part 2 solution"""
    result = 0
    for f in first:
        score = 0
        for s in second:
            if f == s:
                score+= 1
        result+= int(f) * score

    print(f"Part2: {result}")

part1(first_list, second_list)
part2(first_list, second_list)

