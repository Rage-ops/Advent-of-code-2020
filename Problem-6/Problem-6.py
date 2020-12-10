# Advent of Code 2020 Day 6

out, out2 = 0, 0
with open("Problem-6/Day 6: Custom Customs.txt") as file:
    data = file.read().split("\n\n")
    for group in data:
        d = {}
        members = 1
        for char in group:
            if char != '\n':
                d[char] = d.get(char, 0) + 1
            else:
                members += 1
        for letter, count in d.items():
            if letter != '\n' and count == members:
                out2 += 1
            out += 1
print(f"Part1: Sum of counts: {out}")
print(f"Part2: Sum of counts: {out2}")


