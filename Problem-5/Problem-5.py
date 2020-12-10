# Advent of Code 2020 Day 5

def decode(text, low, high, head, tail):
    for i in range(len(text) - 1):
        mid = (low + high) // 2
        if text[i] == head:
            high = mid
        elif text[i] == tail:
            low = mid + 1
        i += 1
    return low if text[-1] == head else high


with open("Problem-5/Day 5: Binary Boarding.txt") as file:
    data = file.read().split("\n")
    m = 0
    d = {}
    for i in range(1025):
        d[i] = False
    for seat_code in data:
        row = decode(seat_code[:7], 0, 127, 'F', 'B')
        column = decode(seat_code[-3:], 0, 7, 'L', 'R')
        m = max(m, row * 8 + column)
        d[row * 8 + column] = True

print(f"Part 1: Highest Seat ID: {m}")
for i in range(1025):
    if not d[i]:
        if 1024 > i > 0 and d[i - 1] and d[i + 1]:
            print(f"Part 2: ID of the seat: {i}")
