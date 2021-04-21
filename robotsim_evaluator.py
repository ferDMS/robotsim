import sys
import math
import json
from modules.map import Map

robot = None
crashed = False
reset = False
start = True

with open('resources/map.json') as json_file:
    map_info = json.load(json_file)


class Robot:
    def __init__(self, col: int, row: int, direction: int) -> None:
        self.dir = direction
        self.col = col
        self.row = row
        self.movements = 0
        self.logic_calls = 0
        self.points = 0
        self.red_color_identified = False
        self.green_color_identified = False
        self.finished = False

    def move_forward(self) -> None:
        if self.finished:
            return
        if self._get_distance(0):
            self.movements += 1
            factor = ((-1, 0), (0, -1), (1, 0), (0, 1))
            self.row += factor[self.dir][0]
            self.col += factor[self.dir][1]
            print('Moving forward, total movements:', self.movements)
        return

    def rotate_right(self) -> None:
        if self.finished:
            return
        self.movements += 1
        self.dir = (self.dir - 1 + 4) % 4
        print('Rotating right, total movements:', self.movements)
        return

    def rotate_left(self) -> None:
        if self.finished:
            return
        self.movements += 1
        self.dir = (self.dir + 1) % 4
        print('Rotating left, total movements:', self.movements)
        return

    def ultrasonic_front(self) -> int:
        if self.finished:
            return -1
        self.logic_calls += 1
        return self._get_distance(0)

    def ultrasonic_right(self) -> int:
        if self.finished:
            return -1
        self.logic_calls += 1
        return self._get_distance(1)

    def ultrasonic_left(self) -> int:
        if self.finished:
            return -1
        self.logic_calls += 1
        return self._get_distance(2)

    def _get_distance(self, dir_ultrasonic: int) -> int:
        dirs = [[0, 1, 2, 3],
                [3, 0, 1, 2],
                [1, 2, 3, 0]]
        distance = None
        start_dist = 0
        distance_direction = dirs[dir_ultrasonic][self.dir]
        if distance_direction == 0:
            for row in range(self.row, -1, -1):
                if game_map.tiles[row][self.col].north.status == 1:
                    distance = start_dist
                    break
                start_dist += 1
            if distance is None:
                return -1
        if distance_direction == 1:
            for col in range(self.col, -1, -1):
                if game_map.tiles[self.row][col].west.status == 1:
                    distance = start_dist
                    break
                start_dist += 1
            if distance is None:
                return -1
        if distance_direction == 2:
            for row in range(self.row, game_map.height):
                if game_map.tiles[row][self.col].south.status == 1:
                    distance = start_dist
                    break
                start_dist += 1
            if distance is None:
                return -1
        if distance_direction == 3:
            for col in range(self.col, game_map.width):
                if game_map.tiles[self.row][col].east.status == 1:
                    distance = start_dist
                    break
                start_dist += 1
            if distance is None:
                return -1
        return distance

    def get_color(self) -> str:
        if self.finished:
            return ''
        self.logic_calls += 1
        row = self.row
        col = self.col
        if game_map.tiles[row][col].color:
            return game_map.tiles[row][col].color
        return 'white'

    def display_color(self, color: str) -> None:
        if self.finished:
            return
        self.logic_calls += 1
        row = self.row
        col = self.col
        tile_color = game_map.tiles[row][col].color
        if not game_map.tiles[row][col].color_identified and color == tile_color:
            game_map.tiles[row][col].color_identified = True
            if color == 'blue':
                self.points += 10
                print(f'+10 Color successfully identified: {color} ', "Total points:", self.points)
            elif color == 'red':
                self.red_color_identified = True
                self.points += 25
                print(f'+25 Color successfully identified: {color} ', "Total points:", self.points)
            elif color == 'green':
                self.green_color_identified = True
                self.points += 25
                print(f'+25 Color successfully identified: {color} ', "Total points:", self.points)
            handle_finish_tile_change()
        return

    def scan_front(self) -> bool:
        if self.finished:
            return False
        self.logic_calls += 1
        row = self.row
        col = self.col
        if self.dir == 0 and row-1 > -1:
            return game_map.tiles[row-1][col].object
        if self.dir == 1 and col-1 > -1:
            return game_map.tiles[row][col-1].object
        if self.dir == 2 and row+1 < game_map.height:
            return game_map.tiles[row+1][col].object
        if self.dir == 3 and col+1 < game_map.width:
            return game_map.tiles[row][col+1].object
        return False

    def grab_obj(self) -> None:
        if self.finished:
            return
        self.movements += 1
        row = self.row
        col = self.col
        if self.dir == 0 and row-1 > -1 and game_map.tiles[row-1][col].object:
            game_map.tiles[row-1][col].object = False
            self.points += 10
            print(f'+10 Object grabbed', "Total points:", self.points)
        if self.dir == 1 and col-1 > -1 and game_map.tiles[row][col-1].object:
            game_map.tiles[row][col-1].object = False
            self.points += 10
            print(f'+10 Object grabbed', "Total points:", self.points)
        if self.dir == 2 and row+1 < game_map.height and game_map.tiles[row+1][col].object:
            game_map.tiles[row+1][col].object = False
            self.points += 10
            print(f'+10 Object grabbed', "Total points:", self.points)
        if self.dir == 3 and col+1 < game_map.width and game_map.tiles[row][col+1].object:
            game_map.tiles[row][col+1].object = False
            self.points += 10
            print(f'+10 Object grabbed', "Total points:", self.points)
        return

    def finish_round(self) -> None:
        self.logic_calls -= 1
        if self.get_color() == 'magenta':
            self.points += 60
            print('Arrived correctly to exit: +60')
        self.finished = True
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Program finished!')
        print("Total points: ", self.points)
        print("Total movements: ", self.movements)
        print("Total logic calls: ", self.logic_calls)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return

    def debug_tile(self) -> None:
        print("(~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)")
        print("Color: ", game_map.tiles[self.row][self.col].color)
        print("north: ", game_map.tiles[self.row][self.col].north.status)
        print("south: ", game_map.tiles[self.row][self.col].south.status)
        print("east: ", game_map.tiles[self.row][self.col].east.status)
        print("west: ", game_map.tiles[self.row][self.col].west.status)
        print("(~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)")
        return

def handle_finish_tile_change() -> None:
    row_finish_tile = game_map.finish_tile_position[0]
    col_finish_tile = game_map.finish_tile_position[1]
    if not is_valid_coordinate(row_finish_tile, col_finish_tile):
        return
    direction = ["north", "south", "east", "west"]
    dir_reflection = ["south", "north", "west", "east"]
    dir_reflection_xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if robot.red_color_identified and robot.green_color_identified:
        for dir_index in range(len(direction)):
            setattr(getattr(game_map.tiles[row_finish_tile][col_finish_tile],
                            direction[dir_index]), "status", 0)
            new_row = row_finish_tile + dir_reflection_xy[dir_index][0]
            new_col = col_finish_tile + dir_reflection_xy[dir_index][1]
            if is_valid_coordinate(new_row, new_col):
                setattr(getattr(game_map.tiles[new_row][new_col],
                                dir_reflection[dir_index]), "status", 0)
    return

def is_valid_coordinate(row: int, col: int) -> bool:
    if row >= game_map.height or row < 0:
        return False
    if col >= game_map.width or col < 0:
        return False
    return True


def setup_map() -> None:
    global game_map
    game_map = Map(map_info['size']['w'], map_info['size']['h'])
    direction = ["north", "south", "east", "west"]
    dir_reflection = ["south", "north", "west", "east"]
    dir_reflection_xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if map_info['finish_tile']:
        game_map.finish_tile_position = (
            map_info['finish_tile']['row'], map_info['finish_tile']['col'])
        map_info['tiles'].append({
            "row": game_map.finish_tile_position[0],
            "col": game_map.finish_tile_position[1],
            "color": "magenta",
            "directions": [1, 1, 1, 1],
            "object": False
        })
    for tile in map_info['tiles']:
        game_map.tiles[tile['row']][tile['col']].color = tile['color']
        game_map.tiles[tile['row']][tile['col']].object = tile['object']
        for dir_index in range(len(direction)):
            if getattr(getattr(game_map.tiles[tile['row']][tile['col']],
                               direction[dir_index]), "status") == 0:
                setattr(getattr(game_map.tiles[tile['row']][tile['col']],
                                direction[dir_index]), "status", tile['directions'][dir_index])
            if tile['directions'][dir_index]:
                new_row = tile['row'] + dir_reflection_xy[dir_index][0]
                new_col = tile['col'] + dir_reflection_xy[dir_index][1]
                if is_valid_coordinate(new_row, new_col):
                    setattr(getattr(game_map.tiles[new_row][new_col],
                                    dir_reflection[dir_index]), "status", 1)
    for i in range(map_info['size']['w']):
        game_map.tiles[0][i].north.status = 1
        game_map.tiles[map_info['size']['h']-1][i].south.status = 1
    for i in range(map_info['size']['h']):
        game_map.tiles[i][0].west.status = 1
        game_map.tiles[i][map_info['size']['w']-1].east.status = 1
    return

def setup_robot() -> None:
    global robot
    global robot_img
    global robot_blue
    global robot_red
    global robot_green
    col = map_info['robot_start']['col']
    row = map_info['robot_start']['row']
    angle = map_info['robot_start']['w']
    dic_dir = {0: 3, 90: 0, 180: 1, 270: 2}
    direction = dic_dir[angle]
    robot = Robot(col, row, direction)
    return

def main() -> None:
    setup_map()
    setup_robot()
    with open("main_program.py") as f:
        code = compile(f.read(), "main_program.py", 'exec')
        exec(code)
    return

if __name__ == "__main__":
    main()
