from utils import get_lines
from typing import List

DAYS_IN_CYCLE = 9
RESET_TO_DAY = 6
SPAWN_TO_DAY = 8


def day6_part1(filename="input.txt", num_days=80):
    return simulate(num_days, filename)


def day6_part2(filename="input.txt", num_days=256):
    return simulate(num_days, filename)


def simulate(num_days: int, filename="input.txt"):
    lines = get_lines(filename)
    starter_fish_list = lines[0].split(",")
    # print(starter_fish_list)
    lanternfish = [0] * DAYS_IN_CYCLE
    start(lanternfish, starter_fish_list)
    # print(lanternfish)
    run(lanternfish, num_days)
    return sum(lanternfish)


def start(result: List[int], input: List[str]):
    for numstr in input:
        result[int(numstr)] += 1


def run(result: List[int], n: int):
    for _ in range(n):
        reached_zero = result[0]
        for i in range(len(result) - 1):
            result[i] = result[i + 1]
        result[RESET_TO_DAY] += reached_zero
        result[SPAWN_TO_DAY] = reached_zero


if __name__ == "__main__":
    print("DAY 1")
    print(f"TEST-INPUT: {day6_part1('test-input.txt')}")
    print(f"REAL INPUT: {day6_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {day6_part2('test-input.txt')}")
    print(f"REAL INPUT: {day6_part2()}")

