N = int(input())
dir_arr = [list(input().split()) for _ in range(N)]
Dir_dic = {'W':0, 'S':1, 'N':2, 'E':3}

for i in range(N):
    dir_arr[i][1] = int(dir_arr[i][1])

def isStart(x,y):
    return x == 0 and y == 0

def loop_true(x,y, counter):
    return (not isStart(x,y)) and counter < N

def move(x,y,dir_char):
    dir_num = Dir_dic[dir_char]
    return x + dx[dir_num], y + dy[dir_num]

dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]
level = 0
counter = 0
nx, ny = 0, 0
first_loop = True

while(first_loop or loop_true(nx,ny,level)):
    first_loop = False
    if dir_arr[level][1] > 0:
        nx, ny = move(nx, ny, dir_arr[level][0])
        counter += 1
        dir_arr[level][1] -= 1
    else: level += 1

if isStart(nx,ny):
    print(counter)
else:
    print("-1")