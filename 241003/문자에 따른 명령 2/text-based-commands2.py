a = input()
dir_num = 0
nx, ny = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for c in a:
    if c == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif c == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        nx += dx[dir_num]
        ny += dy[dir_num]

print(nx, ny)