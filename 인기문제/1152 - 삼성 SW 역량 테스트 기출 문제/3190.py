def printer(input_maze):
    print()
    for i in range(len(input_maze)):
        for j in range(len(input_maze[0])):
            print(input_maze[i][j], end=" ")
        print()


def wall_maker(input_maze):
    input_maze[1][1] = 'x'
    for i in range(len(input_maze)):
        for j in range(len(input_maze[0])):
            if i == 0 or i == len(input_maze) - 1 or j == 0 or j == len(input_maze[0]) - 1:
                input_maze[i][j] = 'x'


def dir_calculate(snake_dir, word):
    left = False
    right = False
    y = 0
    x = 0

    if snake_dir[0] != 0:
        left = True
    elif snake_dir[1] != 0:
        right = True

    if word == 'D':
        if left:
            y = snake_dir[1]
            x = snake_dir[0] * -1
        elif right:
            y = snake_dir[1]
            x = snake_dir[0]
    elif word == 'L':
        if left:
            y = snake_dir[1]
            x = snake_dir[0]
        elif right:
            y = snake_dir[1]
            x = snake_dir[0] * -1

    return y, x


maze_length = int(input())
maze = [['0' for i in range(maze_length + 2)] for j in range(maze_length + 2)]
snake_position = [[1, 1]]
snake_dir = [0, 1]
clock = 0

wall_maker(maze)

apple_num = int(input())
for i in range(apple_num):
    apple_y, apple_x = map(int, input().split())
    maze[apple_y][apple_x] = 'a'

move_num = int(input())

turn_list = dict()

for i in range(move_num):
    move, dir = input().split()
    move = int(move)
    turn_list[move] = dir

while True:
    new_pos = [snake_position[0][0] + snake_dir[0], snake_position[0][1] + snake_dir[1]]
    clock += 1

    if maze[new_pos[0]][new_pos[1]] == 'a':
        maze[new_pos[0]][new_pos[1]] = 'x'
        snake_position.insert(0, new_pos)
        if clock in turn_list:
            snake_dir = dir_calculate(snake_dir, turn_list[clock])
        # snake_position.append([tail_y, tail_x])
        # maze[tail_y][tail_x] = 'x'
    elif maze[new_pos[0]][new_pos[1]] == '0':
        maze[new_pos[0]][new_pos[1]] = 'x'
        snake_position.insert(0, new_pos)
        tail_y, tail_x = snake_position.pop()
        maze[tail_y][tail_x] = '0'
        if clock in turn_list:
            snake_dir = dir_calculate(snake_dir, turn_list[clock])
    else:
        break
print(clock)


