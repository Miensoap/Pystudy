def move(x,y,dir_num):
    dx,dy = [0,1,-1,0],[1,0,0,-1]
    nx,ny= x+dx[dir_num],y+dy[dir_num]
    return nx,ny

def in_range(nx,ny,n):
    return 0<=nx<n and 0<=ny<n

n,t=map(int,input().split())
r,c,d=input().split()
x,y=int(r)-1,int(c)-1
arr1=[['o' for _ in range(n)] for _ in range(n)]

dir={'R':0,'L':3,'U':2,'D':1}
# c_dir={'R':2,'L':1,'U':3,'D':0}
move_cnt=t
dir_num=dir[d]

while move_cnt:
    move_cnt-=1
    x,y=move(x,y,dir_num)
    if not in_range(x,y,n) :
        dir_num= 3-dir_num
        x,y=move(x,y,dir_num)
        

print(x+1,y+1)
    
