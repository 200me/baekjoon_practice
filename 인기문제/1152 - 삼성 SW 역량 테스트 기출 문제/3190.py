def printer(input_maze):
    for i in range(len(input_maze)):
        for j in range(len(input_maze[0])):
            print(input_maze[i][j], end=" ")
        print()


def wall_maker(input_maze):
    for i in range(len(input_maze)):
        for j in range(len(input_maze[0])):
            if i == 0 or i == len(input_maze) - 1 or j == 0 or j == len(input_maze[0]) - 1:
                input_maze[i][j] = 'x'


maze_length = int(input())
maze = [[0 for i in range(maze_length + 2)] for j in range(maze_length + 2)]
snake_position = [0, 0]
clock = 0

wall_maker(maze)
printer(maze)






