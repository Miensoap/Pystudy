x, y = 0,0
dir_num=3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def move1(dir_num) :
    global x,y
    if dir_num == 0:
        x, y = x + dx[0], y + dy[0]
    elif dir_num == 1:
        x, y = x + dx[1], y + dy[1]
    elif dir_num == 2:
        x, y = x + dx[2], y + dy[2]
    else:
        x, y = x + dx[3], y + dy[3]

def rotate(D):
    global dir_num
    if D=='R':
        dir_num = (dir_num + 1) % 4
    elif D=='L':
        dir_num = (dir_num+3)%4

arr=list(input())

for i in range(len(arr)):
    if arr[i]=='F':
        move1(dir_num)
    else:
        rotate(arr[i])

print(x,y)
    
