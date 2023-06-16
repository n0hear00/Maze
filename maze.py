# Open / read file of the first maze
file = open("maze-task-first.txt", "r")
maze = file.readlines()

# Variable declarations
start = None
goal = None
visited = set()
path = []
max_moves = 200


def get_neighbors(row, col):
    neighbors = []

    # Check up
    if row - 1 >= 0 and maze[row - 1][col] != '#':
        neighbors.append((row - 1, col))

    # Check down
    if row + 1 < len(maze) and maze[row + 1][col] != '#':
        neighbors.append((row + 1, col))

    # Check left
    if col - 1 >= 0 and maze[row][col - 1] != '#':
        neighbors.append((row, col - 1))

    # Check right
    if col + 1 < len(maze[0]) and maze[row][col + 1] != '#':
        neighbors.append((row, col + 1))

    return neighbors


def dfs(row, col, moves):
    if moves > max_moves:
        return False

    if (row, col) == goal:
        return True

    visited.add((row, col))

    for neighbor in get_neighbors(row, col):
        if neighbor not in visited:
            if dfs(neighbor[0], neighbor[1], moves + 1):
                path.append((row, col))
                return True

    return False


# Get start and end coordinates
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '^':
            start = (i, j)
        elif maze[i][j] == 'E':
            goal = (i, j)

if dfs(start[0], start[1], 0):
    # Add the correct path to the maze
    for position in path:
        row, col = position
        maze[row] = maze[row][:col] + '.' + maze[row][col + 1:]

    # Save finished maze to .txt file
    with open("first_maze_solution.txt", "w") as output_file:
        for row in maze:
            output_file.write(row)

    print("Solution of the first maze saved to 'maze_solution.txt'!")
else:
    print("Path not found within", max_moves)
   






# Open / read file of the first maze
file = open("maze-task-second.txt", "r")
maze = file.readlines()

# Variable declarations for second maze
start = None
goal = None
visited = set()
path = []
max_moves = 200

# Get start and end coordinates
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '^':
            start = (i, j)
        elif maze[i][j] == 'E':
            goal = (i, j)
            
if dfs(start[0], start[1], 0):
    # Add the correct path to the maze
    for position in path:
        row, col = position
        maze[row] = maze[row][:col] + '.' + maze[row][col + 1:]

    # Save finished maze to .txt file
    with open("maze_solution_second.txt", "w") as output_file:
        for row in maze:
            output_file.write(row)

    print("Solution of the second maze saved to 'maze_solution.txt'!")
else:
    print("Path not found within", max_moves, "for the second maze")
