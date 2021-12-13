from utils import get_lines
from typing import List, DefaultDict, Set
from collections import defaultdict, Counter


def day12_part1(filename="input.txt"):
    lines = get_lines(filename)
    edges = [line.strip().split("-") for line in lines]
    adj_list = defaultdict(list)

    # build adjacency list
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    # backtrack
    routes = []
    curr_route = ["start"]
    visited = {"start"}
    backtrack(adj_list, routes, curr_route, visited, "start")
    return len(routes)


def backtrack(adj_list: DefaultDict[str, List[str]], routes: List[List[str]], curr_route: List[str], visited: Set[str], current: str):
    if current == "end":
        routes.append(curr_route.copy())
        # print(curr_route)
        return

    for dest in adj_list[current]:
        if dest.isupper() or dest not in visited:
            curr_route.append(dest)
            if dest.islower():
                visited.add(dest)
            backtrack(adj_list, routes, curr_route, visited, dest)
            curr_route.pop()
            if dest.islower():
                visited.remove(dest)


def day12_part2(filename="input.txt"):
    lines = get_lines(filename)
    edges = [line.strip().split("-") for line in lines]
    adj_list = defaultdict(list)

    # build adjacency list
    for a, b in edges:
        if b == "start":
            a, b = b, a
        adj_list[a].append(b)
        if a != "start":
            adj_list[b].append(a)

    # backtrack
    routes = []
    curr_route = ["start"]
    visited = set()
    visited.add("start")
    backtrack2(adj_list, routes, curr_route, visited, "start", False)
    return len(routes)


def backtrack2(adj_list: DefaultDict[str, List[str]], routes: List[List[str]], curr_route: List[str], visited, current: str, used_twice: bool):
    if current == "end":
        routes.append(curr_route.copy())
        # print(",".join(curr_route))
        return

    for dest in adj_list[current]:
        if dest.isupper() or dest not in visited:
            curr_route.append(dest)
            if dest.islower():
                visited.add(dest)
            backtrack2(adj_list, routes, curr_route, visited, dest, used_twice)
            curr_route.pop()
            if dest.islower():
                visited.remove(dest)
        elif dest != "start" and not used_twice:
            curr_route.append(dest)
            backtrack2(adj_list, routes, curr_route, visited, dest, True)
            curr_route.pop()


if __name__ == "__main__":
    print("PART 1")
    print(f"TEST-INPUT: {day12_part1('test-input.txt')}")
    print(f"TEST-INPUT2: {day12_part1('test-input2.txt')}")
    print(f"TEST-INPUT3: {day12_part1('test-input3.txt')}")
    print(f"REAL INPUT: {day12_part1()}")
    print("PART 2")
    print(f"TEST-INPUT: {day12_part2('test-input.txt')}")
    print(f"TEST-INPUT2: {day12_part2('test-input2.txt')}")
    print(f"TEST-INPUT3: {day12_part2('test-input3.txt')}")
    print(f"REAL INPUT: {day12_part2()}")

