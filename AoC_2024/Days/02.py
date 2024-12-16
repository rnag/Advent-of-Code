"""
--- Day 2: Red-Nosed Reports ---

Link:
    https://adventofcode.com/2024/day/2

"""
from pathlib import Path


# Input: Reports
INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# TODO: Update filename `input` and uncomment once ready!
# INPUT = open(Path(__file__).parent / "input").read()


def remap(reports) -> list[list[int]]:
    """
    Remap example list input provided in "Advent of Code"
    format, to two separate lists.

    e.g. input as element pairs from each list seperated
    by three spaces, each on a new line.

    """
    _l1 = []
    _l2 = []
    return [[int(level) for level in report.split(' ')]
           for report in reports.strip().split('\n')]


def num_of_safe_reports(reports: list[list[int]]) -> int:
    """
    Solution to Day 2 [Part 1]

    *How many reports are safe?*
    """
    num_safe = 0

    for report in reports:
        last_level = report[0]
        # If last level is greater than the first level,
        # then the levels are increasing, so the difference
        # between levels should be 0 or positive.
        is_positive = report[-1] > last_level

        for level in report[1:]:
            if (is_positive != (level > last_level)
                    or not 0 < abs(level - last_level) < 4):
                break
            last_level = level
        else:
            num_safe += 1

    return num_safe


def _is_valid(prev_level: int, level: int, is_positive: bool) -> bool:
    return (is_positive == (level > prev_level)
            and 0 < abs(level - prev_level) < 4)


def num_of_safe_reports_with_problem_dampener(
        reports: list[list[int]]) -> int:
    """
    Solution to Day 2 [Part 2]

    *How many reports are safe with the problem dampener?*
    """
    num_safe = 0

    for report in reports:
        last_level = report[0]
        # If last level is greater than the first level,
        # then the levels are increasing, so the difference
        # between levels should be 0 or positive.
        is_positive = report[-1] > last_level
        # The Problem Dampener allows the reactor safety systems
        # to tolerate a *single* bad level!
        problem_dampener_activated = False

        for i, level in enumerate(report[1:], start=1):
            if level == last_level:
                if problem_dampener_activated:
                    break
                problem_dampener_activated = True
            elif (is_positive != (level > last_level)
                  or not 0 < abs(level - last_level) < 4):
                if problem_dampener_activated:
                    break
                problem_dampener_activated = True
                # does removing the current level make the report valid?
                if i == len(report) - 1 or _is_valid(
                        report[i - 1], report[i + 1], is_positive):
                    continue
                # does removing the previous level make the report valid?
                if i != 1 and not _is_valid(
                        report[i - 2], level, is_positive):
                    # we can't fix it with the problem dampener alone
                    # (which tolerates a *single* bad level)
                    break
            last_level = level
        else:
            num_safe += 1

    return num_safe


if __name__ == '__main__':
    _reports = remap(INPUT)

    # Part 1
    print('Part 1:  ', num_of_safe_reports(_reports))
    # Part 2
    print('Part 2:  ', num_of_safe_reports_with_problem_dampener(_reports))
