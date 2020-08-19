'''
Movement:
    robot.move_forward()
    robot.move_backward()
    robot.rotate_right()
    robot.rotate_left()

Sensors:
    robot.ultrasonic_forward() -> int
    robot.ultrasonic_left() -> int
    robot.ultrasonic_right() ->int
    robot.ultrasonic_back() -> int
    robot.get_color() -> string
'''

def main():
    def rotate_90_left():
        for i in range(90):
            robot.rotate_left()

    for i in range(4):
        while(robot.ultrasonic_forward() > 25):
            robot.move_forward()
            print( robot.ultrasonic_left(),robot.ultrasonic_right())
        rotate_90_left()

if __name__ == "__main__":
    main()