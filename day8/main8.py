from utils import get_lines
from typing import List, Dict


def day8_part1(filename="input.txt"):
    lines = get_lines(filename)
    ten_digits, output = [], []
    total_count = 0
    for line in lines:
        first, second = line.split("|")
        ten_digits.append(first.strip().split(" "))
        output.append(second.strip().split(" "))
    i = 0
    for td, out in zip(ten_digits, output):
        searching_for = set()
        for digit_str in td:
            if 2 <= len(digit_str) <= 4 or len(digit_str) == 7:
                searching_for.add(sort(digit_str))
        for digit in out:
            if sort(digit) in searching_for:
                total_count += 1
        i += 1
    return total_count


def sort(s: str) -> str:
    to_list = list(s)
    to_list.sort()
    return "".join(to_list)


def day8_part2(filename="input.txt"):
    lines = get_lines(filename)
    ten_digits, output = [], []
    total_sum = 0
    for line in lines:
        first, second = line.split("|")
        ten_digits.append(first.strip().split(" "))
        output.append(second.strip().split(" "))
    for td, out in zip(ten_digits, output):
        d = dict()
        make_map(d, td)
        # print(d)
        curr_num = 0
        for digit in out:
            curr_num = (curr_num * 10) + d[sort(digit)]
        total_sum += curr_num
    return total_sum


def make_map(d: Dict[str, int], digits: List[str]):
    # print(digits)
    remaining = set(digits)
    opposite = dict()
    # find 1, 4, 7, 9
    to_remove = set()
    for digit in remaining:
        if len(digit) == 2:
            d[sort(digit)] = 1
            opposite[1] = sort(digit)
            to_remove.add(digit)
        elif len(digit) == 3:
            d[sort(digit)] = 7
            opposite[7] = sort(digit)
            to_remove.add(digit)
        elif len(digit) == 4:
            d[sort(digit)] = 4
            opposite[4] = sort(digit)
            to_remove.add(digit)
        elif len(digit) == 7:
            d[sort(digit)] = 8
            opposite[8] = sort(digit)
            to_remove.add(digit)
    remaining.difference_update(to_remove)

    # find 0, 6, 9
    to_remove = set()
    for digit in remaining:
        if len(digit) == 6:
            digit_set = set(digit)
            if digit_set > set(opposite[1]) and digit_set > set(opposite[4]):
                d[sort(digit)] = 9
                opposite[9] = sort(digit)
                to_remove.add(digit)
            elif digit_set > set(opposite[1]):
                d[sort(digit)] = 0
                opposite[0] = sort(digit)
                to_remove.add(digit)
            else:
                d[sort(digit)] = 6
                opposite[6] = sort(digit)
                to_remove.add(digit)
    remaining.difference_update(to_remove)

    for digit in remaining:
        if set(digit) > set(opposite[7]):
            d[sort(digit)] = 3
        elif len(set(opposite[9]) - set(digit)) == 1:
            d[sort(digit)] = 5
        else:
            d[sort(digit)] = 2


if __name__ == "__main__":
    # print("DAY 1")
    # print(f"TEST-INPUT: {day8_part1('test-input.txt')}")
    # print(f"REAL INPUT: {day8_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {day8_part2('test-input.txt')}")
    print(f"REAL INPUT: {day8_part2()}")

