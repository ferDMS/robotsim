'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.display_color(string)
    robot.finish_round()
Sensors:
    robot.ultrasonic_front() -> int
    robot.ultrasonic_right() -> int
    robot.ultrasonic_left() -> int
    robot.get_color() -> string
'''

def main():
    class Vertex:
        # Constructor receives x : int, y : int, color : str
        def __init__(self, x = None, y = None, color = None):
            self.x = x              # X coordinate
            self.y = y              # Y coordinate
            self.color = color      # Color of the vertex
            self.visited = False    # Has the vertex been visited?
            self.adj = dict()       # Adjacent vertices ("up", "down", "left", "right")


        # Overloading the equality operator == between two Vertex objects
        def __eq__(self, other) -> bool:
            return (self.x == other.x and self.y == other.y)
        

        # Defining the hashing arguments for usage of Vertex objects as dictionary (hashmap) keys
        def __hash__(self):
            return hash(self.x) ^ hash(self.y)
        

        # Add an undirected edge on the direction specified
        # Method receives v : Vertex object, dir : str
        def addEdge(self, v, dir):
            if (dir == "left"):
                self.adj["left"] = v
                v.adj["right"] = self
            elif (dir == "right"):
                self.adj["right"] = v
                v.adj["left"] = self
            elif (dir == "up"):
                self.adj["up"] = v
                v.adj["down"] = self
            elif (dir == "down"):
                self.adj["down"] = v
                v.adj["up"] = self
            else:
                print("Invalid direction to add edge")


        # Return a Vertex object adjacent to this object, shifted to a certain direction
        def shifted(self, dir: str):
            if (dir == "up"):
                return Vertex(self.x, self.y + 1)
            elif (dir == "left"):
                return Vertex(self.x - 1, self.y)
            elif (dir == "down"):
                return Vertex(self.x, self.y - 1)
            elif (dir == "right"):
                return Vertex(self.x + 1, self.y)
            
            print ("Invalid shift direction")
            return None
        

        # Return the string formatted coordinates of the vertex as (x, y)
        def coords(self) -> str:
            return "(" + str(self.x) + ", " + str(self.y) + ")"


    class Graph:
        # Constructor should receive either: 
        #   The number of vertices n : int
        #   A list of vertices vertices : list[Vertex]
        def __init__(self, verticesIn):

            if isinstance(verticesIn, int):
                self.n = verticesIn
                self.vertices = [Vertex() for i in range(n)]
                self.visited = [False] * self.n

            if isinstance(verticesIn, list):
                self.n = len(verticesIn)
                self.vertices = verticesIn
                self.visited = [False] * self.n


        # Bracket [] operator overload to obtain:
        #   The vertex saved object : Vertex, at the specified index : int
        #   The vertex saved object : Vertex, at the specified coordinates : Vertex
        def __getitem__(self, key) -> Vertex:
            
            if isinstance(key, int):
                return self.vertices[key]
            
            if isinstance(key, Vertex):
                for i in range(self.n):
                    if key == self.vertices[i]:
                        return self.vertices[i]
                print("Vertex not found")
                return None


        # Perform graph traversal to find the shortest path from source to destination vertices
        # Returns a list of Vertex objects, where the first should be the source and the last one the destination
        def path(self, source: Vertex, destination: Vertex):
            
            # If the source vertex is the same as the destination vertex, then don't even run the whole algorithm
            if (source == destination):
                return [source]
            
            # Initialize queue as a list to store queued vertices
            queue = []

            # At the start no vertex has been visited
            visited = {v : False for v in self.vertices}

            # At the start no vertex has been found a parent vertex
            parent = {v : None for v in self.vertices}

            # Enqueue the vertex object with source coordinates saved on self.vertices
            queue.append(self[source])
            visited[source] = True

            # Perform Breath First Search
            while not (len(queue) == 0):
                current = queue.pop(0)

                if (current == destination):
                    # Reconstruct the path by getting the parent of each vertex
                    path = []

                    while not (current == source):
                        path.append(current)
                        current = parent[current]

                    path.append(source)  # Append the source vertex to the path
                    path.reverse()  # Reverse the path so it goes from source to destination
                    return path

                # For every adjacent vertex
                for v in current.adj: 
                    neighbor = current.adj[v]

                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
                        parent[neighbor] = current

            # If no path is found, return an empty list
            print("No path was found, returning empty list")
            return []
        

    class MyRobot:
        # Constructor for each instance. Starting position will always be at a vertex with coordinates (0, 0)
        def __init__(self):
            self.color = self.getColor()
            self.pos = Vertex(0,0)
            self.right = 0
            self.up = 0
            self.left = 0
            self.down = 0
            self.last_traversed = 0


        # Change the current robot's facing to a specified direction
        def face(self, dir : str):
            if (self.facing == dir): return
            
            if (dir == "up"):
                if (self.facing == "right"):
                    robot.rotate_left()
                elif (self.facing == "down"):
                    robot.rotate_right()
                    robot.rotate_right()
                elif (self.facing == "left"):
                    robot.rotate_right()
            
            if (dir == "down"):
                if (self.facing == "right"):
                    robot.rotate_right()
                elif (self.facing == "up"):
                    robot.rotate_right()
                    robot.rotate_right()
                elif (self.facing == "left"):
                    robot.rotate_left()

            if (dir == "left"):
                if (self.facing == "right"):
                    robot.rotate_right()
                    robot.rotate_right()
                elif (self.facing == "up"):
                    robot.rotate_left()
                elif (self.facing == "down"):
                    robot.rotate_right()

            if (dir == "right"):
                if (self.facing == "left"):
                    robot.rotate_right()
                    robot.rotate_right()
                elif (self.facing == "up"):
                    robot.rotate_right()
                elif (self.facing == "down"):
                    robot.rotate_left()


        # Move forward
        def move(self):
            robot.move_forward()


        # Turn on the led in the robot with a certain color
        def led(self, color : str):
            robot.display_color(color)

        
        # Get the color of the square in which the robot is standing
        def getColor(self):
            return robot.get_color()


        # Call the ultrasonics to obtain the distances of the robot to the nearest wall in all directions
        def getAllDistances(self):
            if (self.facing == "right"):
                self.up = robot.ultrasonic_left()
                self.right = robot.ultrasonic_front()
                self.down = robot.ultrasonic_right()
                self.left = self.left + self.last_traversed

            elif (self.facing == "up"):
                self.left = robot.ultrasonic_left()
                self.up = robot.ultrasonic_front()
                self.right = robot.ultrasonic_right()
                self.down = self.down + self.last_traversed

            elif (self.facing == "left"):
                self.down = robot.ultrasonic_left()
                self.left = robot.ultrasonic_front()
                self.up = robot.ultrasonic_right()
                self.right = self.right + self.last_traversed

            elif (self.facing == "down"):
                self.right = robot.ultrasonic_left()
                self.down = robot.ultrasonic_front()
                self.left = robot.ultrasonic_right()
                self.up = self.up + self.last_traversed
            
            self.last_traversed = 0


        # Receives a path (list of Vertex object) and traverses it
        # Returns whether the path traversal was successful or not
        def traverse(self, path) -> bool:
            if (len(path) == 0):
                print("Invalid path: Path is empty")
                return False
            elif ( len(path) == 1 and not path[0] == self.pos ):
                print("Invalid path: Path does not start at the current robot's position")
                return False
            elif (len(path) == 1):
                print("Destination vertex is the same as the current position")
                return True

  
            for i in range(len(path)-1):
                for dir in ["right", "up", "left", "down"]:
                    if (path[i].shifted(dir) == path[i+1]):
                        self.face(dir)
                        self.move()
                        self.pos = path[i+1]
                        self.facing = dir
                        break

            return True


        # Turn off the robot / finish the round
        def done(self):
            robot.finish_round()


    # Initialize an instance of my own robot class
    r = MyRobot()

    # At the start the facing of the robot is always down and its vertex position is (0, 0)
    r.facing = "down"
    r.pos = Vertex(0,0)

    # Vertex location of the white square (defined once it is found)
    white_pos = Vertex()

    # Initialize appearance counters for each color
    colors = {
        "red" : 0,
        "blue" : 0,
        "green" : 0,
        "magenta" : 0,
        "yellow" : 0,
        "cyan" : 0
    }

    # Initialize the vertices coordinates of the graph
    vertices = []
    for i in range(0, -6, -1):
        for j in range (0, -8, -1):
            vertices.append(Vertex(i, j))
            print("Vertex: " + Vertex(i,j).coords())

    # Initialize graph object with the vertices list
    g = Graph(vertices)

    # Initialize stack as a list where vertices are inserted at the beginning
    stack = []

    # Initialized the previously visited vertex as the starting vertex at 0, 0
    prev = g[Vertex(0,0)]

    # Push the starting vertex as the first vertex to visit in the stack
    stack.append(prev)

    # Start traversal of graph until all vertices have been visited
    while not (len(stack) == 0):
        # The current vertex is the one that will be visited this iteration
        current = stack.pop( len(stack)-1 )
        print("Starting loop iteration for vertex at " + current.coords())

        # The stack should only contain unvisited vertices, except for vertices found two times from different edges
        # To avoid visiting repeated vertices more than once, we skip the iteration if the vertex is visited
        if current.visited:
            print("Skipping iteration: Already visited")
            continue
        
        # If it hasn't been visited, it will be visited this iteration
        current.visited = True

        # Calculate path to visit the current vertex
        print("Calculating path")
        path = g.path(prev, current)

        # Make the robot traverse the found path
        print("Traversing path")
        r.traverse(path)
        print("Now in current vertex")

        # Once in the current vertex, get the square's color
        r.color = r.getColor()
        current.color = r.color
        print("Found color: " + r.color)

        # If the square is the white square, then save the square's location for later
        if r.color == "white":
            print("Found white square location at " + current.coords())
            white_pos = current
        # If the square is any other color, add an appearance to that color
        else: 
            colors[r.color] += 1
        
        # Display the color on the robot
        r.led(r.color)

        # Get adjacent vertices in all directions to nearest walls using ultrasonics
        r.getAllDistances()
        if (r.left > 0):
            current.addEdge(g[current.shifted("left")], "left")
            print("Adjacent vertex found: " + current.shifted("left").coords())
        if (r.up > 0):
            current.addEdge(g[current.shifted("up")], "up")
            print("Adjacent vertex found: " + current.shifted("up").coords())
        if (r.right > 0):
            current.addEdge(g[current.shifted("right")], "right")
            print("Adjacent vertex found: " + current.shifted("right").coords())
        if (r.down > 0):
            current.addEdge(g[current.shifted("down")], "down")
            print("Adjacent vertex found: " + current.shifted("down").coords())

        # Add adjacent vertices to stack in correct priority order
        # The correct priority order is the one that allows the robot to perform movements that allow it to traverse the greatest
        # amount of vertices that are compacted together (simulating something similar to a BFS, but not exactly). Thus, as the starting
        # vertex is on the top right corner, the priority hierarchy will be up - right - left - down
        # The priority must be input in the reverse order as the structure is a stack, not a queue
        for dir in ["down", "left", "right", "up"]:
            if not (current.adj.get(dir) is None) and not current.adj[dir].visited:
                stack.append(current.adj[dir])
        
        # Save the current vertex as the previous vertex for the next iteration
        print("Setting current vertex as previous vertex")
        prev = current
        print("\n")

    print("\n\nExplored all vertices")

    # Go to the white vertex location
    print("Going to the white square location")
    path = g.path(prev, white_pos)
    r.traverse(path)
    
    # Obtain the missing color (the only color with incomplete appearances of 7)
    missing = ""
    for color, count in colors.items():
        if count == 7:
            missing = str(color)
    g[white_pos].color = missing
    print("The missing color is " + missing)

    # Display the missing color
    r.led(missing)
    
    # Initialize the exit square's position as the top left corner (according to the coordinate format provided)
    exit_pos = Vertex(-6, 1)
    
    # Calculate the exit square x coordinate (column)
    print("Calculating x coordinate of exit square")
    # For each column
    for i in range(0, -6, -1):
        # Restart count of colors to 0
        colors = {color : 0 for color in colors}
        # If on the column where the white square is located, reduce its color count by one
        if (white_pos.x == i):
            colors[g[white_pos].color] -= 1
        # For each square in the column (row)
        for j in range(0, -8, -1):
            # Add an appearance of the square's color
            colors[g[Vertex(i,j)].color] += 1
        # Keep track of unique color appearances
        unique_colors = 0
        # The +1 point for 3+ appearances can only be given once
        unique_above_three = False
        for count in colors.values():
            # If a color has 3 or more appearances, the exit square is 1 more column right
            if (count >= 3 and not unique_above_three):
                unique_above_three = True
                exit_pos = exit_pos.shifted("right")
            # If each color is found at least once in the column, the exit square is 2 more columns right
            if (count > 0):
                unique_colors += 1
                if (unique_colors == 6):
                    exit_pos = exit_pos.shifted("right").shifted("right")

    # Calculate the exit square y coordinate (row)
    print("Calculating y coordinate of exit square")
    # For each row
    for i in range(0, -8, -1):
        # Restart count of colors to 0
        colors = {color : 0 for color in colors}
        # If on the row where the white square is located, reduce its color count by one
        if (white_pos.y == i):
            colors[g[white_pos].color] -= 1
        # For each square in the row (column)
        for j in range(0, -6, -1):
            # Add an appearance of the square's color
            colors[g[Vertex(j,i)].color] += 1
        # Keep track of unique color appearances
        unique_colors = 0
        # The +1 point for 3+ appearances can only be given once
        unique_above_three = False
        for count in colors.values():
            # If a color has 3 or more appearances, the exit square is 1 more row down
            if (count >= 3 and not unique_above_three):
                unique_above_three = True
                exit_pos = exit_pos.shifted("down")
            # If each color is found at least once in the row, the exit square is 2 more rows down
            if (count > 0):
                unique_colors += 1
                if (unique_colors == 6):
                    exit_pos = exit_pos.shifted("down").shifted("down")

    # Go to the exit vertex location
    print("Going to the exit square location at " + exit_pos.coords())
    path = g.path(white_pos, exit_pos)
    r.traverse(path)

    # Finally exit the maze :)
    r.done()


if __name__ == "__main__":
    main()