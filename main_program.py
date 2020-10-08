'''
Movement:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()

Sensors:
    robot.ultrasonicFront() -> int
    robot.getColor() -> string
    robot.detectSimbolLeft() -> int
    robot.detectSimbolRight() -> int
    robot.detectDoorFront() -> bool
    robot.insertCode(password) -> int
'''

def main():
    robot.debugTile()
    print(robot.ultrasonicFront())
    robot.rotate_right()
    for _ in range(2):
        robot.move_forward()
        robot.debugTile()
    print(robot.ultrasonicFront())
    print(robot.insertCode("011"))
    print(robot.ultrasonicFront())
    robot.move_forward()
    robot.debugTile()
    # print(robot.getColor())
    # print(robot.detectSimbolRight())
    # robot.rotate_left()
    # print(robot.detectDoorFront())

if __name__ == "__main__":
    main()