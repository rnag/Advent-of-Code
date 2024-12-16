"""
--- Day 5: Print Queue ---

Link:
    https://adventofcode.com/2024/day/5

"""
from pathlib import Path

INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# TODO: Update filename `input` and uncomment once ready!
# INPUT = open(Path(__file__).parent / "input").read()


def remap(sections: str) -> tuple[
    list[tuple[int, int]],
    list[list[int]]
]:
    """
    Remap example list input provided in "Advent of Code"
    format, to two separate lists.
    """
    _order_rules, _updates = sections.strip().split('\n\n')

    order_rules = [tuple(map(int, r.split('|'))) for r in _order_rules.split('\n')]

    updates = [[int(u) for u in update.split(',')] for update in _updates.split('\n')]

    # noinspection PyTypeChecker
    return order_rules, updates


def sum_of_middle_page_nums(order_rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    """
    Solution to Part 1

    *What do you get if you add up the middle page number from those correctly-ordered updates?*
    """
    valid_updates = []

    for update in updates:
        for (before, after) in order_rules:
            try:
                idx1 = update.index(before)
                idx2 = update.index(after)
            except ValueError:
                continue
            else:
                if idx1 >= idx2:
                    break
        else:
            valid_updates.append(update)

    count = 0
    for update in valid_updates:
        count += update[len(update) // 2]

    return count


def sum_of_middle_page_nums_for_invalid_updates(order_rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    """
    Solution to Part 2

    *What do you get if you add up the middle page numbers after correctly ordering just those updates?*
    """
    invalid_updates = []

    for update in updates:
        is_invalid = False
        for (before, after) in order_rules:
            try:
                idx1 = update.index(before)
                idx2 = update.index(after)
            except ValueError:
                continue
            else:
                if idx1 >= idx2:
                    is_invalid = True
                    break
        if is_invalid:
            invalid_updates.append(update)

    count = 0

    for update in invalid_updates:
        update_to_idx = {u: i for i, u in enumerate(update)}
        while True:
            for (before, after) in order_rules:
                try:
                    before_idx = update_to_idx[before]
                    after_idx = update_to_idx[after]
                except KeyError:
                    continue
                if before_idx >= after_idx:
                    update_to_idx[before], update_to_idx[after] = after_idx, before_idx
                    break
            else:
                break

        mid_idx = len(update) // 2
        for update, idx in update_to_idx.items():
            if idx == mid_idx:
                count += update
                break

    return count


if __name__ == '__main__':

    _order_rules, _updates = remap(INPUT)
    # Part 1
    print('Part 1:  ', sum_of_middle_page_nums(_order_rules, _updates))
    # Part 2
    print('Part 2:  ', sum_of_middle_page_nums_for_invalid_updates(_order_rules, _updates))
