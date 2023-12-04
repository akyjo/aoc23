from functools import reduce
from collections import defaultdict

f = open("day2_input.txt", "r")
lines = f.readlines()
max_cubes = {'red':12, 'green':13, 'blue':14}
#lines processing
lines = [line.split(':')[1][1:] for line in lines]
lines = [line.replace(';', ',').replace('\n', '').replace(', ', ',') for line in lines]
games = [line.split(',') for line in lines]
print(games)
def possible_with_max_cubes(game):
    for round in game:
        value, color = round.split(' ')
        if max_cubes[color] >= int(value):
            ...
        else:
            return False
    return True
# part1 solution
# filtered = filter(possible_with_max_cubes, games)

# sum = 0
# for i,_ in enumerate(games, 1):
#     if possible_with_max_cubes(_):
#         sum += i
# print(sum)
def fewest_cubes(game):
    colors = defaultdict(lambda : 0)
    for round in game:
        value, color = round.split(' ')
        if colors[color] < int(value):
            colors[color] = int(value)
    return reduce(lambda x,y: x*y, colors.values())

print(sum([fewest_cubes(game) for game in games]))
