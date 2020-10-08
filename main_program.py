'''
Movement:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()

Sensors:
    robot.ultrasonicFront() -> None
    robot.getColor() -> string
    robot.detectSimbolLeft() -> int
    robot.detectSimbolRight() -> int
    robot.detectDoorFront() -> bool
    robot.insertCode() -> int
'''

def main():
    for _ in range(4):
        robot.move_forward()
    print(robot.getColor())
    print(robot.detectSimbolRight())
    robot.rotate_left()
    print(robot.detectDoorFront())

if __name__ == "__main__":
    main()