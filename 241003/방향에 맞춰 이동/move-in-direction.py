N = int(input())

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
nx, ny = 0, 0

for i in range(N):
    dir_temp, dis_temp = input().split()
    if dir_temp == 'W':
        dir_temp = 0
    elif dir_temp == 'S':
        dir_temp = 1
    elif dir_temp == 'N':
        dir_temp = 2
    else:
        dir_temp = 3
    nx += (int(dis_temp) * dx[dir_temp])
    ny += (int(dis_temp) * dy[dir_temp])
print(nx, ny)