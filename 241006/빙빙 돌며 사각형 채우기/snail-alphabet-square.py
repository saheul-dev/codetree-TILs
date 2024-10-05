n, m = map(int, input().split())

def num2char(num):
    num = num % (ord('Z') - ord('A') + 1) + ord('A')
    return chr(num)

class Squr:
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    def __init__(self, n, m):
        self.n, self.m = n, m
        self.s = [[0 for _ in range(m)] for _ in range(n)]
        self.nx = 0
        self.ny = 0
        self.dir_num = 0
        self.counter = 0

    def in_range(self):
        x, y = self.next_xy()
        return 0 <= x < self.m and 0<= y < self.n

    def can_move(self):
        x, y = self.next_xy()
        return self.in_range() and self.s[y][x] == 0

    def next_xy(self):
        return self.nx + self.dx[self.dir_num], self.ny + self.dy[self.dir_num]

    def turn_dir(self):
        self.dir_num = (self.dir_num + 1) % 4
    
    def fill(self):
        self.s[self.ny][self.nx] = num2char(self.counter)
        self.counter += 1
    
    def move(self):
        self.nx, self.ny = self.next_xy()

    def start(self):
        if not self.can_move():
            self.turn_dir()
        while(self.can_move()):
            self.fill()
            self.move()
            if not self.can_move():
                self.turn_dir()
        self.fill()
        self.print_squr()
            

    def print_xy(self):
        print(self.nx, self.ny)

    def print_squr(self):
        for i in range(self.n):
            for j in range(self.m):
                print(f"{self.s[i][j]} ", end="")
            print()

s = Squr(n, m)

s.start()