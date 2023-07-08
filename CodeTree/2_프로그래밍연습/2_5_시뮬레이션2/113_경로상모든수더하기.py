def movef(x,y):
    dx, dy = [0,1,0,-1], [-1,0,1,0]
    nx , ny = x+dx[dir_num], y+dy[dir_num]
    if in_range(nx,ny):
        return nx,ny,True
    else:
        return x,y,False
    
def in_range(x,y):
    global n
    if 0<=x<n and 0<=y<n :
        return True

def ro_move (cm):
    global dir_num,x,y,ans
    if cm == 'R' :
        dir_num=(dir_num+1)%4 # cw
    elif cm =='L':
        dir_num=(dir_num+3)%4 # ccw
    elif cm =='F':
        x,y,k = movef(x,y)
        if k : 
            ans+=arr1[y][x]
    

n,m=map(int,input().split())
mv=list(input())
arr1=[list(map(int,input().split())) for _ in range(n)]
x, y = n//2 , n//2
dir_num=0
ans=arr1[y][x]

for i in range(m):
    cm=mv[i]
    ro_move(cm)

print(ans)

    
