from utils import get_lines
from typing import List, Dict
from collections import Counter


def parse_input(filename: str) -> (Dict[str, str], List[str]):
    lines = get_lines(filename)
    template = list(lines[0].strip())
    rules = dict()
    for i in range(2, len(lines)):
        key, val = lines[i].strip().split(" -> ")
        rules[key] = val
    return rules, template


def day14_part1(filename="input.txt"):
    rules, template = parse_input(filename)
    for i in range(10):
        template = step(rules, template)
    counts = Counter(template).most_common()
    return counts[0][1] - counts[-1][1]


def step(rules, template):
    new_template = []
    for i in range(1, len(template)):
        key = "".join(template[i - 1: i + 1])
        new_template.append(template[i - 1])
        new_template.append(rules[key])
    new_template.append(template[-1])
    return new_template


def day14_part2(filename="input.txt"):
    rules, template = parse_input(filename)
    counts = Counter()

    # create counter for adjacent characters
    for i in range(1, len(template)):
        key = "".join(template[i - 1: i + 1])
        counts[key] += 1

    for i in range(40):
        counts = step_part2(rules, counts)
        get_max_min_counts(counts, template[0], template[-1])

    max_count, min_count = get_max_min_counts(counts, template[0], template[-1])

    return max_count - min_count


def step_part2(rules, counts):
    new_counts = Counter()
    for key, count in counts.items():
        val = rules[key]
        a, b = key[0], key[1]
        new_counts[a + val] += count
        new_counts[val + b] += count
    return new_counts


def get_max_min_counts(counts, first, last):
    counter = Counter()
    for key, val in counts.items():
        a, b = key[0], key[1]
        counter[a] += val
        counter[b] += val

    # Do not double count adjacent characters
    for key, val in counter.items():
        counter[key] = counter[key] // 2
    # First and last weren't double counted, add back
    counter[first] += 1
    counter[last] += 1

    counter_as_list = counter.most_common()
    return counter_as_list[0][1], counter_as_list[-1][1]


if __name__ == "__main__":
    print("DAY 1")
    print(f"TEST-INPUT: {day14_part1('test-input.txt')}")
    print(f"REAL INPUT: {day14_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {day14_part2('test-input.txt')}")
    print(f"REAL INPUT: {day14_part2()}")

