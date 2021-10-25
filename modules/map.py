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
        self.north = Direction()
        self.south = Direction()
        self.east = Direction()
        self.west = Direction()
        self.color_identified = False
        self.touched = False

class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.tiles = [[Tile() for _ in range(width)] for _ in range(height)]
        self.finish_tile_position = (-1, -1)