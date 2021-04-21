import json
import random

height = 20
width = 30
colored_tile = random.randint(0, 30)
object_in_tile = random.randint(0, 60)
posible_walls = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
]

game_map = {}
game_map["squareSize"] = 30
game_map["size"] = {"w": width, "h": height}
game_map["robot_start"] = {"row": 0, "col": 0, "w": 0}
game_map["tiles"] = []

for row in range(height):
    for col in range(width):
        tile = {}
        color = "blue" if colored_tile == random.randint(0, 30) else "white"
        object_placed = object_in_tile == random.randint(0, 60)
        walls = random.randint(1, 20)
        directions = posible_walls[walls] if walls < 10 else posible_walls[0]
        tile = {
            "row": row,
            "col": col,
            "color": color,
            "object": object_placed,
            "directions": directions,
        }
        game_map["tiles"].append(tile)

special_tiles = [(0, 0)]
while len(special_tiles) < 4:
    row = random.randint(0, height - 1)
    col = random.randint(0, width - 1)
    if (row, col) not in special_tiles:
        special_tiles.append((row, col))

game_map["tiles"][special_tiles[1][0]*height + special_tiles[1][1]]["color"] = "red"
game_map["tiles"][special_tiles[2][0]*height + special_tiles[2][1]]["color"] = "green"
game_map["finish_tile"] = {"row": special_tiles[3][0], "col": special_tiles[3][1]}

with open('resources/map1.json', 'w') as outfile:
    json.dump(game_map, outfile)
