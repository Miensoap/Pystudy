import sys
n=int(input())
arr=[list(sys.stdin.readline().rstrip())for _ in range(n)]
m=int(input())
dir_num=1
x, y = 0,0
cnt=0

def move(x,y):
    dx, dy = [0,1,0,-1], [-1,0,1,0]
    nx , ny = x+dx[dir_num], y+dy[dir_num]
    if in_range(nx,ny):
        return nx,ny
    else:
        return -1,-1
    
def in_range(x,y):
    global n
    if 0<=x<n and 0<=y<n :
        return True

def reflect ():
    global dir_num,x,y
    if arr[y][x] == '/' :
        if dir_num == 0 or dir_num ==2:
           dir_num=(dir_num+1)%4 # cw
        elif dir_num == 1 or dir_num ==3:
            dir_num=(dir_num+3)%4 # ccw
    elif arr[y][x] == '\\' : 
        if dir_num == 1 or dir_num ==3:
            dir_num=(dir_num+1)%4 # cw
        elif dir_num == 0 or dir_num ==2:
            dir_num=(dir_num+3)%4 # ccw


#시작위치
for i in range(m-1):
    nx,ny = move(x,y)
    if nx==-1:
        dir_num=(dir_num+1)%4 # cw
    else :
        x,y=nx,ny

if m<=n:
    dir_num=2
elif m<=2*n :
    dir_num=3
elif m<=3*n:
    dir_num=0
else:
    dir_num=1

reflect()
cnt+=1
while x != -1:    
    x,y = move(x,y)
    if x == -1:
        break
    reflect()
    cnt+=1

print(cnt)

# /  :  up,down -> cw , r l -> ccw 
# \  :  u d ->  ccw , r l -> cw

# cw

# 위 -> 오른쪽 -> 아래 -> 왼쪽
# 0 -1   1 0       0 1   -1 0

# (dir_num+1)%4 : 3->0 ->1 ->2 ->3 


# 2 re 1 mo re 2 mo re 1 mo 

# 10      20      21      31 