class Ant():

    def __init__(self, start_x, start_y, start_dir, TILEMAP, maze) -> None:

        self.dist = 0
        self.tilemap = TILEMAP
        self.maze = maze
        self.x = start_x
        self.y = start_y
        self.dir = start_dir

    def move(self, direction):

        if self.dist != 0:
            ...
        if direction == "NORTH":
            self.y = self.y - 1
        if direction == "SOUTH":
            self.y = self.y + 1
        if direction == "WEST":
            self.x = self.x - 1
        if direction == "EAST":
            self.x = self.x + 1

        self.dist += 1

    def get_tile(self) -> str:
        return self.maze[self.y][self.x]

    def get_dir(self):
        rev = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
        came_from = rev[self.dir]
        dirs = self.tilemap[self.get_tile()]
        self.dir = dirs.difference({came_from}).pop()

