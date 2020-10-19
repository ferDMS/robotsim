'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.insertCode(password) -> int

Sensors:
    robot.ultrasonicFront() -> int
    robot.getColor() -> string
    robot.detectSimbolLeft() -> string
    robot.detectSimbolRight() -> string
    robot.detectDoorFront() -> bool
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
    #get Huffman root node
    root = robot.getHuffmanTree()
    answer = ""
    #add decode code here
    print("Decoded answer: ", answer)

if __name__ == "__main__":
    main()