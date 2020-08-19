# robotSim

## About this project
This project has the intention to provide an easy and accesible way for students to learn robotics. 
This project runs a simulation of a robot in which the user can program its movements across a field and receive input from sensors.
<!-- Due to the Covid-19 pandemic teaching robotics without hands-on projects has become challenging -->

## Using the simulator

What's great about robotSim? To start using it you do not need any development enviorement installed to run the program. You simply run *robotsim.exe* and the simulator should start. 
To program the robot movements and read the sensors values you can modify the file *main_program.py*. 
After that simply press the **play button** inside the simululator window and watch your robot run your program!

You can keep the simulator open and modify your code in *main_program.py* each time before pressing the play button, the simulator will run your new code.

The language for writing code in *main_program.py* is Python 3, so you should be somewhat familiar with Python. 
You can declare variables, write your own functions, print in console and everything else you would do in your own python code. 

### Warning

When writing code in *main_program.py* please do so inside the *main()* function whithin the file, if you are making a function, make it a nested function, if you are declaring a variable, declare it inside *main()*.
Hopefully this can be fixed in the future, but for the time being please do this to prevent the program from crashing.

## The robot
Feel free to use any image you like as your robot. Just make sure to place it in the correct folder and name it *robot.png*. 
I highly recomend you use a transparent PNG file image, and also make it square in size since the program resizes it.

To move the robot you have a list of available functions, calling this functions makes the robot move in the simulator.

| Function               | Description                               |
| ---------------------- | ----------------------------------------- |
| robot.move_forward()   | The robot moves one pixel forward         |
| robot.move_backwards() | The robot moves one pixel backward        |
| robot.rotate_right()   | The robot rotates one degree to the right |
| robot.rotate_left()    | The robot rotates one degree to the right |

You can also use the sensors available and get their values
| Function                   | Value type | Description                                                                   |
| -------------------------- | ---------- | ----------------------------------------------------------------------------- |
| robot.ultrasonic_forward() | int        | Returns the distance reading within the range from the **front** of the robot |
| robot.ultrasonic_left()    | int        | Returns the distance reading within the range from the **left** of the robot  |
| robot.ultrasonic_right()   | int        | Returns the distance reading within the range from the **right** of the robot |
| robot.ultrasonic_back()    | int        | Returns the distance reading within the range from the **back** of the robot  |
| robot.get_color()          | string     | Returns the color of the tile in which the robot is currently in.             |

<br>
---

![Simulator screen shot](images\simulator_view.PNG)
