Nchar, Mchar = input().split()
N, M = int(Nchar), int(Mchar)
p = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    rchar, cchar = input().split()
    r, c = int(rchar), int(cchar)
    r, c = r-1, c-1
    p[r][c] = 1
    filled = 0
    if r > 0:
        filled += p[r - 1][c]
    if r < N - 1:
        filled += p[r + 1][c]
    if c > 0:
        filled += p[r][c - 1]
    if c < N - 1:
        filled += p[r][c + 1]
    if filled == 3:
        print("1")
    else:
        print("0")