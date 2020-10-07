import pygame
import json
import math

pixel_constant = 50
display_width = 0
display_height = 0

black = (0,0,0)
white = (255,255,255)
gray = (127,127,127)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
magenta = (255,0,255)
yellow = (255,255,0)
cyan = (0,255,255)

colors = {
    'black' : (0,0,0),
    'white' : (255,255,255),
    'gray' : (127,127,127),
    'red' : (255,0,0),
    'blue' : (0,0,255),
    'green' : (0,255,0),
    'magenta' : (255,0,255),
    'yellow' : (255,255,0),
    'cyan' : (0,255,255)
}

gameDisplay = None
robot = None

pygame.init()
robotImg = pygame.image.load('robot.png')
run_button = pygame.image.load('run.png')
pygame.display.set_caption('Robot simulator')
clock = pygame.time.Clock()

crashed = False
reset = False
start = True

class Robot:
    def __init__(self,x,y,w,size):
        self.x = x
        self.y = y
        self.w = w
        self.size = size
        self.offset = int((pixel_constant - size) * 0.5)
        self.sensor_range = pixel_constant #int(pixel_constant/2)
        self.set_position(x,y,w)
        
    def set_position(self,x,y,w):
        self.x = x
        self.y = y
        self.w = w

        orig_rect = robotImg.get_rect()
        rotated_robot = pygame.transform.rotate(robotImg, w)
        rot_rect = orig_rect.copy()
        rot_rect.center = rotated_robot.get_rect().center
        rotated_robot = rotated_robot.subsurface(rot_rect).copy()

        gameDisplay.blit(rotated_robot, (x + self.offset, y + self.offset))
        # pygame.draw.line(gameDisplay, green, (x-25, y), (x+25, y))
        # pygame.draw.line(gameDisplay, green, (x, y-25), (x, y+25))
        # pygame.draw.line(gameDisplay, red, (x+ int(pixel_constant * 0.5)-25, y + int(pixel_constant * 0.5)), (x+ int(pixel_constant * 0.5)+25, y+ int(pixel_constant * 0.5)))
        # pygame.draw.line(gameDisplay, red, (x+ int(pixel_constant * 0.5), y+ int(pixel_constant * 0.5)-25), (x+ int(pixel_constant * 0.5), y+ int(pixel_constant * 0.5)+25))
        pygame.display.update()
        clock.tick(120)

    def move_forward(self):
        angle = self.w
        x1 = self.x 
        y1 = self.y 
        rad = math.radians(angle)
        x2 = round(math.cos(rad))  + x1
        y2 = y1 - round(math.sin(rad))
        generate_map()
        # Check collisions
        px1 = self.x + int(pixel_constant * 0.5) + round(math.cos(rad)*self.size*0.5) 
        py1 = self.y + int(pixel_constant * 0.5) - round(math.sin(rad)*self.size*0.5)
        for i in range(-int(self.size*0.5)+1,int(self.size*0.5)-1): 
            px2 = round(math.cos(math.radians(90+angle)) * i) + px1
            py2 = py1 - round(math.sin(math.radians(90+angle)) * i)
            is_wall = gameDisplay.get_at((px2,py2)) == colors['black']
            if is_wall:
                return
        self.set_position(x2,y2,angle)

    def move_backward(self):
        angle = self.w
        x1 = self.x 
        y1 = self.y 
        rad = math.radians(angle)
        x2 = x1 - round(math.cos(rad))
        y2 = round(math.sin(rad)) + y1
        generate_map()
        # Check collisions
        px1 = self.x + int(pixel_constant * 0.5) - round(math.cos(rad)*self.size*0.5) 
        py1 = self.y + int(pixel_constant * 0.5) + round(math.sin(rad)*self.size*0.5)
        for i in range(-int(self.size*0.5)+1,int(self.size*0.5)-1): 
            px2 = round(math.cos(math.radians(90+angle)) * i) + px1
            py2 = py1 - round(math.sin(math.radians(90+angle)) * i)
            is_wall = gameDisplay.get_at((px2,py2)) == colors['black']
            if is_wall:
                return
        self.set_position(x2,y2,angle)
    
    def rotate_right(self):
        generate_map()
        self.set_position(self.x,self.y,self.w - 1)

    def rotate_left(self):
        generate_map()
        self.set_position(self.x,self.y,self.w + 1)

    def get_distance(self,angle):
        rad = math.radians(angle)
        x1 = self.x + int(pixel_constant * 0.5) + round(math.cos(rad)*self.size*0.5)
        y1 = self.y + int(pixel_constant * 0.5) - round(math.sin(rad)*self.size*0.5)
        for i in range(self.sensor_range):
            x2 = int(math.cos(math.radians(angle)) * i) + x1
            y2 = y1 - int(math.sin(math.radians(angle)) * i)
            x2 = 0 if x2 < 0 else display_width if x2 > display_width else x2
            y2 = 0 if y2 < 0 else display_height if y2 > display_height else y2
            is_wall = gameDisplay.get_at((x2,y2)) == colors['black']
            pygame.draw.line(gameDisplay, red, (x1, y1), (x2, y2))
            if is_wall:
                pygame.display.update()
                clock.tick(120)
                return i
        return self.sensor_range

    def ultrasonic_forward(self):
        return self.get_distance(self.w)

    def ultrasonic_left(self):
        return self.get_distance(self.w + 90)

    def ultrasonic_back(self):
        return self.get_distance(self.w + 180)

    def ultrasonic_right(self):
        return self.get_distance(self.w + 270)

    def get_color(self):
        x = self.x + int(pixel_constant * 0.5)
        y = self.y + int(pixel_constant * 0.5)
        generate_map()
        c = gameDisplay.get_at((x,y))
        self.set_position(self.x,self.y,self.w)
        for name, value in colors.items():
            if value == c:
                return name


def generate_map():
    gameDisplay.fill(white)

    # Color tiles
    for color in map_info['colors']:
        x = color['x'] * pixel_constant
        y = color['y'] * pixel_constant
        c = colors[color['color']]
        pygame.draw.rect(gameDisplay,c,(x,y,pixel_constant,pixel_constant))

    # Exterior walls
    pygame.draw.line(gameDisplay, colors['black'], (0, 0), (display_width-1, 0))
    pygame.draw.line(gameDisplay, colors['black'], (0, 0), (0, display_height-1))
    pygame.draw.line(gameDisplay, colors['black'], (display_width-1, 0), (display_width-1, display_height-1))
    pygame.draw.line(gameDisplay, colors['black'], (0, display_height-1), (display_width-1, display_height-1))

    # Inner walls
    for wall in map_info['walls']:
        x1 = wall['x1'] * pixel_constant
        x2 = wall['x2'] * pixel_constant
        y1 = wall['y1'] * pixel_constant
        y2 = wall['y2'] * pixel_constant
        if x1 == x2 or y1 == y2: # This ignores diagonal walls
            pygame.draw.line(gameDisplay, colors['black'], (x1, y1), (x2, y2))

            
def setup_map():
    global display_width 
    global display_height 
    global pixel_constant
    global gameDisplay

    pixel_constant = map_info['squareSize'] if map_info['squareSize'] else pixel_constant
    display_width = map_info['size']['w'] * pixel_constant
    display_height = map_info['size']['h'] * pixel_constant

    gameDisplay = pygame.display.set_mode((display_width,display_height))

    generate_map()

def setup_robot():
    global robot
    global robotImg

    robot_size = int(pixel_constant * 0.5)
    robotImg = pygame.transform.scale(robotImg, (robot_size, robot_size))
    
    start_x = map_info['start']['x'] * pixel_constant
    start_y = map_info['start']['y'] * pixel_constant
    angle = map_info['start']['w']

    robot = Robot(start_x,start_y,angle,robot_size)


with open('map.json') as json_file:
    map_info = json.load(json_file)

def main():
    setup_map()
    setup_robot()
    with open("main_program.py") as f:
        code = compile(f.read(), "main_program.py", 'exec')
        exec(code)

if __name__ == "__main__":

    while not crashed:
        if start:
            setup_map()
            setup_robot()
            start = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < pixel_constant * 0.5 and pos[1] < pixel_constant * 0.5:
                    if not reset:
                        reset = True
                
        if reset:
            main()
            reset = False
        else:
            run_button = pygame.transform.scale(run_button, (int(pixel_constant*0.5), int(pixel_constant*0.5)))
            gameDisplay.blit(run_button, (0, 0))
            pygame.display.update()
            clock.tick(120)

    pygame.quit()
    quit()
