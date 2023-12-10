f = open("8data.txt", "r")
from math import lcm
lines = f.readlines()
lines = [line.strip() for line in lines]
move_instr = lines[0]
nodes_map = {line.split(" = (")[0]:(line.split(" = (")[1].replace(")", "").split(", ")) for line in lines[2:]}

i, nodes = 0, []
l_or_r = lambda c: 0 if c == "L" else 1

# brutus
# def advance_1(node, move_index):
#     node = nodes_map[node][l_or_r(move_instr[move_index])]
#     return node

for x in nodes_map.keys():
    if x[2] == "A":
        nodes.append(x)


def p1(node):
    i = 0
    while node[2] != "Z":
        move_index = i % len(move_instr)
        node = nodes_map[node][l_or_r(move_instr[move_index])]
        i+=1
    return i

p1sols = []
for node in nodes:
    p1sols.append(p1(node))
p1tup = tuple(p1sols)
print(p1sols)
print(lcm(*p1tup))


# brutus solutionus
# C = False
#
# while not C:
#     move_index = i % len(move_instr)
#
#     for j in range(len(nodes)):
#         nodes[j] = advance_1(nodes[j], move_index)
#
#     C = all(node[2] == "Z" for node in nodes)
#     i+=1
#
# print(i)
