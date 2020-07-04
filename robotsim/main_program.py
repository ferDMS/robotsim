'''
Movement:
    robot.move_forward()
    robot.move_backwards()
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
    for j in range(4):
        print(robot.get_color())
        for i in range(100):
            robot.move_forward()
        for i in range(90):
            robot.rotate_left()
    # while(robot.ultrasonic_forward() > 25):
    #     robot.move_forward()
    #     print( robot.ultrasonic_left(),robot.ultrasonic_right())


if __name__ == "__main__":
    main()