#!/usr/bin/env python3
"""AOC 2024 Day2"""

import numpy as np

with open("input.txt", "r", encoding="utf-8") as in_data:
    reports = in_data.readlines()
reports = [i.replace("\n", "") for i in reports]


def is_safe(this_report: list) -> bool:
    """Function to decide if report is safe"""
    distance_list = abs(np.diff(this_report))
    print(distance_list)
    for distance in distance_list:
        if distance not in [1, 2, 3]:
            return False

    decreasing = False
    increasing = False
    for i, report_part in enumerate(this_report):
        try:
            if report_part > report[i + 1] and increasing is False:
                decreasing = True
            elif report_part < report[i + 1] and decreasing is False:
                increasing = True
            elif report_part < report[i + 1] and decreasing is True:
                return False
            elif report_part > report[i + 1] and increasing is True:
                return False
        except IndexError:
            continue
    return True


part1_result = 0
part2_result = 0
for report in reports:
    report = [int(i) for i in report.split()]
    print(report)
    match is_safe(report):
        case True:
            print(f"The report {report} is safe")
            part1_result += 1
        case False:
            print(f"The report {report} is not safe")
            for o, value in enumerate(report):
                report.pop(o)
                if is_safe(report) is True:
                    part2_result += 1
                    break
                report.insert(o, value)
print(f"total number of safe report {part1_result}")
print(f"total number of safe report  with Problem Dampener: {part1_result + part2_result}")
