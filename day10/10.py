from ant import Ant
# f = open("10test.txt", "r")
f = open("10.txt", "r")
maze = [line for line in f.readlines()]
start_y, start_x = 0, 0 # so that lsp doesnt cry

for row in maze:
    if "S" in row:
        start_y = maze.index(row)
        for char in row:
            if char == "S":
                start_x = row.index(char)
                break
        break

TILEMAP = {"|" : {"NORTH", "SOUTH"},
           "-" : {"EAST", "WEST"},
           "L" : {"NORTH", "EAST"},
           "J" : {"NORTH", "WEST"},
           "7" : {"WEST", "SOUTH"},
           "F" : {"EAST", "SOUTH"}}

a = Ant(start_x, start_y, "SOUTH", TILEMAP, maze)

while True:
    a.move(a.dir)
    t = a.get_tile()
    if t == "S":
        print(a.dist/2)
        break
    a.get_dir()




















