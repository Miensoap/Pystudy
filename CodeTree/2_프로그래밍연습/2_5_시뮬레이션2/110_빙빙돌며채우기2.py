def move_rotate(x,y):
    global dir_num
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    nx,ny= x+dx[dir_num],y+dy[dir_num]
    
    if in_range(nx,ny,n,m) and arr1[ny][nx] == 'o':
        return nx,ny
    else:
        dir_num=(dir_num+3)%4
        return move_rotate(x,y)

def in_range(nx,ny,n,m):
    return 0<=nx<m and 0<=ny<n

n,m=map(int,input().split()) #가로가m 새로가 n
x,y=0,0
dir_num=2
arr1=[['o' for _ in range(m)] for _ in range(n)]

arr1[0][0]=1
for i in range(1,n*m):
    x,y=move_rotate(x,y)
    arr1[y][x]=i+1


for i in range(n):
    for j in range(m):
        print(arr1[i][j],end=' ')
    print()
    
