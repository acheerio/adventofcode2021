from utils import get_lines
from typing import List
from collections import Counter
import math


def day7_part1(filename="input.txt"):
    lines = get_lines(filename)
    positions = [int(x) for x in lines[0].split(",")]
    max_pos = max(positions)

    # count
    counter = Counter(positions)
    dp = [counter[i] for i in range(max_pos + 1)]

    # position
    min_moves = math.inf
    for i in range(max_pos + 1):
        curr_moves = 0
        for j in range(0, i):
            curr_moves += (dp[j] * (i - j))
        for k in range(i + 1, max_pos + 1):
            curr_moves += (dp[k] * (k - i))
        min_moves = min(min_moves, curr_moves)

    return min_moves


def day7_part2(filename="input.txt"):
    lines = get_lines(filename)
    positions = [int(x) for x in lines[0].split(",")]
    max_pos = max(positions)

    # count
    counter = Counter(positions)
    dp = [counter[i] for i in range(max_pos + 1)]

    # position
    min_moves = math.inf
    for i in range(max_pos + 1):
        curr_moves = 0
        for j in range(0, i):
            n = i - j
            curr_moves += (dp[j] * int(((n*(n+1))/2)))
        for k in range(i + 1, max_pos + 1):
            n = k - i
            curr_moves += (dp[k] * int(((n*(n+1))/2)))
        min_moves = min(min_moves, curr_moves)

    return min_moves


if __name__ == "__main__":
    print("DAY 1")
    print(f"TEST-INPUT: {day7_part1('test-input.txt')}")
    print(f"REAL INPUT: {day7_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {day7_part2('test-input.txt')}")
    print(f"REAL INPUT: {day7_part2()}")


