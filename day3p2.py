from functools import reduce
from pprint import pprint
import re
f = open("day3_data.txt", "r")
lines = f.readlines()
filelen = len(lines)

asterisk_coords = []
for i, line in enumerate(lines):
    for match in re.finditer(r'\*', line):
        asterisk_coords.append([i,  match.start()])

gears= []
for i, coord in enumerate(asterisk_coords):
    gear = []
    for line in lines[max(0, coord[0] - 1): min(filelen, coord[0] + 1) + 1]:
        for match in re.finditer(r'\d+', line):
            if (match.start()-1) <= coord[1] and (match.end() >= coord[1] ):
                gear.append(int(match.group()))
    gears.append(gear)

print(gears)
print(sum([reduce(lambda x,y: x*y, gear) for gear in gears if len(gear) > 1]))


