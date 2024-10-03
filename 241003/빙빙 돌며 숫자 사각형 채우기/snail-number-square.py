n, m = map(int, input().split())
p = [[0 for _ in range(m)] for _ in range(n)]

dx, dy = [0,1,0,-1],[-1,0,1,0]

dir_num = 1
nx, ny = 0, 0

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n
    
def can_move_to(x, y):
    return in_range(x,y) and p[y][x] == 0

def turn_right(dir_num):
    return (dir_num + 1) % 4

def move(x, y, dir_num):
    return x + dx[dir_num], y + dy[dir_num]

def fill(x, y, arr, num):
    arr[y][x] = num

for i in range(m * n):
    fill(nx, ny, p, i+1)
    tmp_x, tmp_y = move(nx, ny, dir_num)
    if not can_move_to(tmp_x, tmp_y):
        dir_num = turn_right(dir_num)
        tmp_x, tmp_y = move(nx, ny, dir_num)
    nx, ny = tmp_x, tmp_y


for i in range(n):
    for j in range(m):
        print("%d " % p[i][j], end="")
    print()