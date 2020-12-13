# Advent of Code 2020 Day 8
import re


with open("Problem-8/Day 8: Handheld Halting.txt") as file:
    data = file.readlines()


def part1(data):
    visited = [False for _ in range(len(data))]
    acc, i = 0, 0
    while not visited[i]:
        op, sign, arg = re.search(
            r"^(acc|jmp|nop) ([+-]{1})(\d+)", data[i]).group(1, 2, 3)
        visited[i] = True
        if op == "acc":
            acc = acc + int(arg) if sign == "+" else acc - int(arg)
            i += 1
        elif op == "jmp":
            i = i + int(arg) if sign == "+" else i - int(arg)
        else:
            i += 1
        if i == len(visited):
            return False, acc
    return True, acc


def part2(data):
    for index, line in enumerate(data):
        match = re.search(r"^(acc|jmp|nop) ([+-]{1})(\d+)", line)
        if match.group(1) == "jmp":
            data[index] = "nop " + data[index][4:]
            res = part1(data)
            data[index] = "jmp " + data[index][4:]
            if not res[0]:
                return res[1]
        elif match.group(1) == "nop":
            data[index] = "jmp " + data[index][4:]
            res = part1(data)
            data[index] = "nop " + data[index][4:]
            if not res[0]:
                return res[1]


print("Part 1: ", part1(data)[1])
print("Part 2: ", part2(data))
