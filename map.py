from enum import IntEnum

class DirectionStatus(IntEnum):
    Free = 0
    Wall = 1

class Direction:
    def __init__(self):
        self.status = DirectionStatus.Free 
        self.data = None
        

class Tile:
    def __init__(self):
        self.color = None
        self.North = Direction()
        self.South = Direction()
        self.East = Direction()
        self.West = Direction()
        self.envType = "clear" # "fire", "people", "collapse", "clear", "safe"
        self.envData = None

class Map:
    def __init__(self, width, height):
        
        self.width = width 
        self.height = height 
        
        self.tiles = [[False for i in range(self.width)] for j in range(self.height)]
        
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x] = Tile()

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
