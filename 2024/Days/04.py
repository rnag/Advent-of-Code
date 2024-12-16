"""
--- Day 4: Ceres Search ---

Link:
    https://adventofcode.com/2024/day/4

"""
from pathlib import Path


INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

SEARCH_WORD = "XMAS"

# TODO: Update filename `input` and uncomment once ready!
# INPUT = open(Path(__file__).parent / "input").read()


def _find_match(line: str, word=SEARCH_WORD):
    return line.count(word) + line[::-1].count(word)


def occurrences_of_word(puzzle, word=SEARCH_WORD) -> int:
    """
    Solution to Part 1

    *How many times does XMAS appear?*
    """
    lines = puzzle.strip().splitlines()
    max_row = len(lines)
    max_col = len(lines[0])
    min_bdiag = -max_row + 1

    count = 0

    # I can't take credit for this mad genius.
    # See https://stackoverflow.com/a/43311126/10237506

    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(lines[y][x])
            rows[y].append(lines[y][x])
            fdiag[x + y].append(lines[y][x])
            bdiag[x - y - min_bdiag].append(lines[y][x])

    for groups in cols, rows, fdiag, bdiag:
        for group in groups:
            line = ''.join(group)
            count += _find_match(line, word)

    return count


def occurrences_of_x_mas(puzzle) -> int:
    """
    Solution to Part 2

    *How many times does an X-MAS appear?*
    """
    lines = puzzle.strip().splitlines()
    max_row = len(lines)
    max_col = len(lines[0])

    count = 0

    # OK, I can take full credit for this mad genius.

    other_letters = {'M', 'S'}

    for r in range(1, max_row - 1):
        for c in range(1, max_col - 1):
            if (lines[r][c] == 'A'
                    and {lines[r - 1][c - 1], lines[r + 1][c + 1]} == other_letters
                    and {lines[r + 1][c - 1], lines[r - 1][c + 1]} == other_letters):
                count += 1

    return count


if __name__ == '__main__':
    # Part 1
    print('Part 1:  ', occurrences_of_word(INPUT))
    # Part 2
    print('Part 2:  ', occurrences_of_x_mas(INPUT))
