import math


def partOne(d):
    diff = {}
    i = 0
    while True:
        if i + 1 in d:
            diff[1] = diff.get(1, 0) + 1
            i += 1
        elif i + 2 in d:
            diff[2] = diff.get(2, 0) + 1
            i += 2
        elif i + 3 in d:
            diff[3] = diff.get(3, 0) + 1
            i += 3
        else:
            break
    return diff[1] * diff[3]


def partTwo(maxi, d):
    paths = [0] * (maxi + 1)
    paths[0] = 1

    for index in range(1, maxi + 1):
        for x in range(1, 4):
            if index - x in d:
                paths[index] += paths[index - x]
    return paths[-1]


if __name__ == "__main__":
    d = {0: None}
    maxi = -math.inf
    with open("Problem-10/Day 10: Adapter Array.txt") as file:
        for index, line in enumerate(file):
            num = int(line.strip("\n"))
            d[num] = None
            maxi = max(maxi, num)
    maxi += 3
    d[maxi] = None
    print(partOne(d))
    print(partTwo(maxi, d))
