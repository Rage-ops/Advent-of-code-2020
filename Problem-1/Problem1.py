#  Advent of Code 2020 Day 1

with open('./Problem-1.txt') as file:
    data = file.read().split('\n')
    arr = sorted([int(ele) for ele in data])

# Solution for part 1
def partOne(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            return l, r
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1

sol = partOne(arr, 2020)
print(arr[sol[0]] * arr[sol[1]])

# Solution for part 2
def partTwo(arr, target):
    d = {}
    for index, val in enumerate(arr, 0):
        d[val] = index
    for key, value in d.items():
        rem = target - key
        sol = partOne(arr, rem)
        if sol:
            if sol[0] != val and sol[1] != val:
                return key * arr[sol[0]] * arr[sol[1]]


print(partTwo(arr, 2020))

