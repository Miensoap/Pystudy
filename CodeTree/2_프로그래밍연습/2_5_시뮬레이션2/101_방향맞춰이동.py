n=int(input())
x, y = 0, 0

def move(dir,d):
    global x, y
    dx, dy = [int(d), 0, -int(d), 0], [0, -int(d), 0, int(d)]

    if dir == 'E':
        x, y = x + dx[0], y + dy[0]
    elif dir =='S':
        x, y = x + dx[1], y + dy[1]
    elif dir == 'W':
        x, y = x + dx[2], y + dy[2]
    else:
        x, y = x + dx[3], y + dy[3]

for _ in range(n):
    move(*input().split())

print(x,y)