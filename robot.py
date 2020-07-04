import first

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
        pygame.draw.line(gameDisplay, green, (x-25, y), (x+25, y))
        pygame.draw.line(gameDisplay, green, (x, y-25), (x, y+25))
        pygame.draw.line(gameDisplay, red, (x+ int(pixel_constant * 0.5)-25, y + int(pixel_constant * 0.5)), (x+ int(pixel_constant * 0.5)+25, y+ int(pixel_constant * 0.5)))
        pygame.draw.line(gameDisplay, red, (x+ int(pixel_constant * 0.5), y+ int(pixel_constant * 0.5)-25), (x+ int(pixel_constant * 0.5), y+ int(pixel_constant * 0.5)+25))
        pygame.display.update()
        clock.tick(120)

    def move_forward(self):
        angle = self.w
        x1 = self.x 
        y1 = self.y 
        rad = math.radians(angle)
        x2 = round(math.cos(rad))  + x1
        y2 = y1 - round(math.sin(rad))
        # print(x1,y1)
        # print(x2,y2)
        generate_map()
        px1 = self.x + int(pixel_constant * 0.5) + round(math.cos(rad)*self.size*0.5) 
        py1 = self.y + int(pixel_constant * 0.5) - round(math.sin(rad)*self.size*0.5)
        for i in range(-int(self.size*0.5),int(self.size*0.5)): 
            px2 = round(math.cos(math.radians(90+angle)) * i) + px1
            py2 = py1 - round(math.sin(math.radians(90+angle)) * i)
            is_wall = gameDisplay.get_at((px2,py2)) == black
            if is_wall:
                return
            # pygame.draw.line(gameDisplay, blue, (px1, py1), (px2, py2))
            # pygame.display.update()
            # clock.tick(60)
        self.set_position(x2,y2,angle)

    def move_backwards(self):
        angle = self.w
        x1 = self.x 
        y1 = self.y 
        rad = math.radians(angle)
        x2 = x1 - round(math.cos(rad))
        y2 = round(math.sin(rad)) + y1
        # print(x1,y1)
        # print(x2,y2)
        generate_map()
        px1 = self.x + int(pixel_constant * 0.5) - round(math.cos(rad)*self.size*0.5) 
        py1 = self.y + int(pixel_constant * 0.5) + round(math.sin(rad)*self.size*0.5)
        for i in range(-int(self.size*0.5),int(self.size*0.5)): 
            px2 = round(math.cos(math.radians(90+angle)) * i) + px1
            py2 = py1 - round(math.sin(math.radians(90+angle)) * i)
            is_wall = gameDisplay.get_at((px2,py2)) == black
            if is_wall:
                return
            # pygame.draw.line(gameDisplay, blue, (px1, py1), (px2, py2))
            # pygame.display.update()
            # clock.tick(60)
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
            is_wall = gameDisplay.get_at((x2,y2)) == black
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