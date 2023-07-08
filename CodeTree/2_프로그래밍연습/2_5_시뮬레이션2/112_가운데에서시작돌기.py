def move_rotate(x,y):
    global dir_num
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    nx,ny= x+dx[dir_num],y+dy[dir_num]
    
    if in_range(nx,ny,n) :
        return nx,ny
    else :
        return x,y

def in_range(nx,ny,n):
    return 0<=nx<n and 0<=ny<n

n=int(input()) 
x,y=n//2,n//2
dir_num=0
arr1=[['o' for _ in range(n)] for _ in range(n)]

arr1[y][x]=1
k=1
num=2
flag=False
while True:
    for i in range(int(k)):
        if not 'o' in arr1[n-1]:
            flag=True
            break
        x,y=move_rotate(x,y)
        arr1[y][x]=num
        num+=1
    dir_num=(dir_num+3)%4
    k+=0.5
    if flag:
        break

for i in range(n):
    for j in range(n):
        print(arr1[i][j],end=' ')
    print()


