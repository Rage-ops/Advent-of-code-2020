# Advent of Code 2020 Day 7
import re


adj = {}
visited = {}
with open("Problem-7/Day 7: Handy Haversacks.txt") as file:
    for line in file:
        outer_bag, innerbags = line.split("contain ")
        innerbags = re.findall(r"(\d{1,}) ([a-z ]+) bag|bags", innerbags)
        visited[outer_bag[:-6]] = False
        if outer_bag[:-6] not in adj:
            adj[outer_bag[:-6]] = {}
        for count, bag in innerbags:
            if count and bag:
                if bag not in adj:
                    adj[bag] = {}
                adj[outer_bag[:-6]][bag] = int(count)


def part_one(adj, visited, bag_name):
    def dfs(adj, visited, start, count):
        for edge in adj_reverse[start].keys():
            if not visited[edge]:
                visited[edge] = True
                count = dfs(adj_reverse, visited, edge, count + 1)
        return count

    adj_reverse = {}
    for outer, inner in adj.items():
        if outer not in adj_reverse:
            adj_reverse[outer] = {}
        for key, count in inner.items():
            if key in adj_reverse:
                adj_reverse[key][outer] = count
            else:
                adj_reverse[key] = {outer: count}
    return dfs(adj_reverse, visited, bag_name, 0)


print("Part 1: Total number of bag colors that contain at least one shiny gold bag :",
      part_one(adj, visited, "shiny gold"))


def part_two(adj, start, count):
    if not adj[start]:
        return 0
    temp = 0
    for edge, c in adj[start].items():
        temp += c + c * part_two(adj, edge, count)
    count += temp
    return count


print("Part 2: Shiny gold bag contains total {} number of bags".format(
    part_two(adj, "shiny gold", 0)))
