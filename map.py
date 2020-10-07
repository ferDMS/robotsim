import enum

class DirectionStatus(enum.Enum):
    Free = 0
    Wall = 1
    Door = 2

class Direction:
    def __init__(self):
        self.status = DirectionStatus.Free 
        self.password = None
        self.symbol = None
        

class Tile:
    def __init__(self):
        self.color = None
        self.North = Direction()
        self.South = Direction()
        self.East = Direction()
        self.West = Direction()

class Map:
    def __init__(self, width, height):
        
        self.width = width 
        self.height = height 

        self.tiles = [[False] * self.width] * self.height
        
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x] = Tile()