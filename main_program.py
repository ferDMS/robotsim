'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.display_color(string)
    robot.finish_round()
    robot.grab_obj()

Sensors:
    robot.ultrasonicFront() -> int
    robot.getColor() -> string
    robot.scan_front() -> bool
'''

def main():
    robot.move_forward()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_right()
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