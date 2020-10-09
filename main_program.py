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
    robot.move_forward()
    robot.insertCode("101")
    robot.rotate_right()
    robot.insertCode("101")
    robot.rotate_right()
    robot.insertCode("101")
    robot.rotate_right()
    robot.insertCode("101")
    robot.rotate_right()
    robot.move_forward()

if __name__ == "__main__":
    main()