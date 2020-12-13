# Advent of Code 2020 Day 9
with open("Problem-9/Day 9: Encoding Error.txt") as file:
    data = file.readlines()


def partOne(data):
    d = {}
    for i in range(25):
        l = []
        for j in range(i + 1, 25):
            l.append(int(data[i]) + int(data[j]))
        d[i] = l

    for idx, number in enumerate(data[25:], 25):
        d[idx] = []
        flag = False
        for values in d.values():
            if int(number) in values:
                flag = True
                break
        if not flag:
            return int(number)
        del d[idx - 25]
        for i in range(idx - 24, idx):
            d[i].append(int(data[i]) + int(number))


def partTwo(data, target):
    cumsum = {}
    curr = 0
    for idx, number in enumerate(data):
        number = int(number)
        curr += number
        cumsum[curr] = idx
        if curr - target in cumsum:
            return int(max(data[cumsum[curr - target] + 1:idx + 1])) + int(min(data[cumsum[curr - target] + 1:idx + 1]))


res = partOne(data)
print("Part 1:", res)
print("Part 2:", partTwo(data, res))
