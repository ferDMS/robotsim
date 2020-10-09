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
    robot.move_forward()
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.insertCode("011")
    robot.move_forward()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.insertCode("110")
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_right()

if __name__ == "__main__":
    main()