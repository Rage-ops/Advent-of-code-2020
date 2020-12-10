# Advent of Code 2020 Day 4

import re

required_keys =  ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
out, out2 = 0, 0

with open("Problem-4/Day 4: Passport Processing.txt") as file:
    data = file.read().split("\n\n")
    for passport in data:
        row = re.sub(r'[\n ]{1,}', ", ", passport) + ","
        d = dict(re.findall(r'([a-z]+):(.*?),', row))
        if all([key in d.keys() for key in required_keys]):
            out += 1
            if (2002 >= int(d['byr']) >= 1920 and 2020 >= int(d['iyr']) >= 2010
                and 2030 >= int(d['eyr']) >= 2020 and d['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                and re.search(r'^#[0-9a-f]{6}$', d['hcl']) and re.match('^\d{9}$', d['pid'])):

                height = d['hgt']
                if (height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193) or (height[-2:] == 'in' and 59 <= int(height[:-2]) <= 76):
                    out2 += 1
print('There are %d valid passports according to part 1.' % out)
print('There are %d valid passports according to part 2.' % out2)
