'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.display_color(string)
    robot.finish_round()
    robot.grab_obj()

Sensors:
    robot.ultrasonic_front() -> int
    robot.getColor() -> string
    robot.scan_front() -> bool
'''

def main():
    robot.move_forward()
    robot.display_color('blue')
    ret = robot.scan_front()
    print(robot.getColor(), ret)
    robot.grab_obj()
    robot.move_forward()
    robot.display_color('red')
    ret = robot.scan_front()
    print(robot.getColor(), ret)
    robot.scan_front()
    robot.move_forward()
    robot.display_color('green')
    robot.display_color('green')
    robot.display_color('green')
    robot.display_color('blue')
    robot.display_color('blue')
    robot.display_color('red')
    robot.getColor()
    robot.ultrasonic_front()
    robot.rotate_right()
    robot.move_forward()
    robot.display_color('red')
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
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.display_color('green')

if __name__ == "__main__":
    main()