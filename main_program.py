from coord import Coord

'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.insertCode(password) -> int

Sensors:
    robot.ultrasonicFront() -> int
    robot.getColor() -> string
    robot.detectSimbolLeft() -> int
    robot.detectSimbolRight() -> int
    robot.detectDoorFront() -> bool
'''

def main():

    ###################################
    #Test 1: Robot eliminado por fuego
    ###################################
    # robot.move_forward()
    # robot.rotate_right()
    # robot.move_forward()
    # robot.rotate_left()
    # robot.move_forward()
    # robot.move_forward()
    # robot.move_forward()


    ###################################
    #Test 2: Robot atrapado en derrumbe
    ###################################
    # robot.move_forward()
    # robot.move_forward()
    # robot.move_forward()
    # robot.rotate_right()
    # robot.move_forward()
    # robot.move_forward()
    # robot.rotate_right()
    # robot.move_forward()
    # robot.rotate_right()
    # robot.rotate_right()
    # robot.move_forward()
    # robot.rotate_right()
    # robot.move_forward()

    ############################################
    #Test 3: Robot apaga fuego y salva personas
    ############################################
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.rotate_left()
    robot.putOutFireFront()
    robot.rotate_right()
    # robot.move_forward()
    # robot.move_forward()
    # robot.move_forward()
    # robot.rotate_right()
    # robot.move_forward()
    # robot.move_forward()
    # print("People saved?",robot.sendMessageRescueBase(Coord(4,3)))
    

if __name__ == "__main__":
    main()