"""
--- Day 1: Historian Hysteria ---

Link:
    https://adventofcode.com/2024/day/1

"""
from pathlib import Path


location_ids = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

# TODO: Update filename `input` and uncomment once ready!
# INPUT = open(Path(__file__).parent / "input").read()


def remap(loc_ids) -> tuple[list[int], list[int]]:
    """
    Remap example list input provided in "Advent of Code"
    format, to two separate lists.

    e.g. input as element pairs from each list seperated
    by three spaces, each on a new line.

    """
    _l1 = []
    _l2 = []
    for _n1, _n2 in [map(int, i.split('   '))
                     for i in loc_ids.strip().split('\n')]:
        _l1.append(_n1)
        _l2.append(_n2)

    return _l1, _l2


def sum_of_distances(l1, l2):
    """
    Solution to Day 1 [Part 1]

    *What is the total distance between your lists?*
    """
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)


    return sum([abs(n1 - n2)
                for n1, n2 in zip(l1_sorted, l2_sorted)])


def similarity_score(_l1, _l2):
    """
    Solution to Day 1 [Part 2]

    *What is the total distance between your lists?*
    """
    score = 0
    score_cache = {}

    for n in _l1:
        if (this_score := score_cache.get(n)) is None:
            this_score = score_cache[n] = n * _l2.count(n)

        score += this_score

    return score


if __name__ == '__main__':
    l1, l2 = remap(location_ids)

    # Part 1
    print('Part 1:  ', sum_of_distances(l1, l2))
    # Part 2
    print('Part 2:  ', similarity_score(l1, l2))
