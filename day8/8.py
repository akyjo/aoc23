f = open("8data.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
move_instr = lines[0]
nodes = {line.split(" = (")[0]:(line.split(" = (")[1].replace(")", "").split(", ")) for line in lines[2:]}

node = "AAA"
i = 0
l_or_r = lambda c: 0 if c == "L" else 1

while node != "ZZZ":
    move_index = i % len(move_instr)
    node = nodes[node][l_or_r(move_instr[move_index])]
    i+=1

print(i)
