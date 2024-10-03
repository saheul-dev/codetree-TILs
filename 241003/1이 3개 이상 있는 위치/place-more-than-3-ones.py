n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
count = 0
res = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(0, n):
    for j in range(0, n):
        for dx, dy in zip(dxs, dys):
            if in_range(j+dx, i+dy) and p[i+dy][j+dx] == 1:
                count += 1
        if count >= 3:
            res += 1
        count = 0

print(res)