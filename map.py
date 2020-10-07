import json
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
    def __init__(self):
        
        with open('map.json') as json_file:
            map_info = json.load(json_file)
	    
        self.width = map_info['size']['w']
        self.height = map_info['size']['h']

        self.tiles = [[False] * self.width] * self.height
        
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x] = Tile()
        
        for wall in map_info['walls']:
            x1 = wall['x1']
            x2 = wall['x2']
            y1 = wall['y1']
            y2 = wall['y2']
            symbol = wall['symbol']
            if x1 == x2:
                if x1 - 1 >= 0 and x1 - 1 <= self.width:
                    self.tiles[y1][x1 - 1].East.status = DirectionStatus.Wall
                    self.tiles[y1][x1 - 1].East.symbol = symbol
                if x1 <= self.width:
                    self.tiles[y1][x1].West.status = DirectionStatus.Wall
                    self.tiles[y1][x1].West.symbol = symbol
            if y1 == y2:
                if y1 - 1 >= 0 and y1 - 1 <= self.height:
                    self.tiles[y1 - 1][x1].South.status = DirectionStatus.Wall
                    self.tiles[y1 - 1][x1].South.symbol = symbol
                if x1 <= self.width:
                    self.tiles[y1 - 1][x1].South.status = DirectionStatus.Wall
                    self.tiles[y1 - 1][x1].South.symbol = symbol
        
        for color in map_info['colors']:
            x = color['x']
            y = color['y']
            color = color['color']
            if y >= 0 and y < self.height and x >= 0 and x < self.width: 
                self.tiles[y][x] = color

        for door in map_info['doors']:
            x1 = door['x1']
            x2 = door['x2']
            y1 = door['y1']
            y2 = door['y2']
            password = door['password']
            if x1 == x2:
                if x1 - 1 >= 0 and x1 - 1 <= self.width:
                    print(y1,x1)
                    self.tiles[y1][x1 - 1].East.status = DirectionStatus.Wall
                    self.tiles[y1][x1 - 1].East.password = password
                if x1 <= self.width:
                    self.tiles[y1][x1].West.status = DirectionStatus.Wall
                    self.tiles[y1][x1].West.password = password
            if y1 == y2:
                if y1 - 1 >= 0 and y1 - 1 <= self.height:
                    self.tiles[y1 - 1][x1].South.status = DirectionStatus.Wall
                    self.tiles[y1 - 1][x1].South.password = password
                if x1 <= self.width:
                    self.tiles[y1 - 1][x1].South.status = DirectionStatus.Wall
                    self.tiles[y1 - 1][x1].South.password = password
             
"""
#Test Map Class Implementation
mymap = Map()
mymap.tiles[0][3].North.status = DirectionStatus.Wall
print(mymap.tiles[0][3].North.status)
"""