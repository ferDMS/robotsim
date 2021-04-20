from enum import IntEnum

class DirectionStatus(IntEnum):
    Free = 0
    Wall = 1

class Direction:
    def __init__(self):
        self.status = DirectionStatus.Free

class Tile:
    def __init__(self):
        self.color = None
        self.North = Direction()
        self.South = Direction()
        self.East = Direction()
        self.West = Direction()
        self.color_identified = False
        self.object = False

class Map:
    def __init__(self, width, height):
        
        self.width = width 
        self.height = height 
        
        self.tiles = [[False for i in range(self.width)] for j in range(self.height)]
        
        self.finish_tile_position = (-1, -1)

        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x] = Tile()