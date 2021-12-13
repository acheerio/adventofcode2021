from utils import get_lines


def day2_part1(filename="input.txt"):
    lines = get_lines(filename)
    # down adds to depth
    hp, depth = 0, 0
    for line in lines:
        command, n = line.split()
        n = int(n) # bad practice, I know
        if command == "forward":
            hp += n
        elif command == "down":
            depth += n
        elif command == "up":
            depth -= n
    print(f"horizontal: {hp} depth: {depth}")
    return hp * depth


def day2_part2(filename="input.txt"):
    lines = get_lines(filename)
    # down adds to depth
    hp, depth, aim = 0, 0, 0
    for line in lines:
        command, n = line.split()
        n = int(n) # bad practice, I know
        if command == "forward":
            hp += n
            depth += aim * n
        elif command == "down":
            aim += n
        elif command == "up":
            aim -= n
    print(f"horizontal: {hp} depth: {depth}")
    return hp * depth


print(day2_part2("input.txt"))
