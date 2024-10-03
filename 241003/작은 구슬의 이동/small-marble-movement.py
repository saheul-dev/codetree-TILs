from enum import Enum

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
nx, ny = c, r

Dir_dic = {'R':0, 'U':1, 'D':2, 'L':3}
dir_num = Dir_dic[d]

while(t > 0):
    nx += dx[dir_num]
    ny += dy[dir_num]

    if nx < 1:
        nx = 1
        dir_num = 3 - dir_num
    elif nx > n:
        nx = n
        dir_num = 3 - dir_num
    elif ny < 1:
        ny = 1
        dir_num = 3 - dir_num
    elif ny > n:
        ny = n
        dir_num = 3 - dir_num

    t -= 1


print(ny, nx)