def move1(x,y,dir_num) :
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    nx,ny = x+dx[dir_num],y+dy[dir_num]
    return nx,ny

def in_range(x,y,n):
    return 0<=x and x<n and 0 <=y and y<n

def test3(x,y,arr):
    cnt=0
    for dir_num in range(4): 
        nx,ny = move1(x,y,dir_num)
        if in_range(nx,ny,n):
            if arr[nx][ny]==1:
                cnt+=1
        if cnt==3:
            return 1
    
    return 0

n,m=map(int,input().split())
chil=[tuple(map(int,input().split()))for _ in range(m)]
arr1 = [[0 for _ in range(n)]for _ in range(n)]
ans=[]

for elem in chil:
    x,y=elem[0]-1,elem[1]-1
    arr1[x][y]=1
    ans.append(test3(x,y,arr1))

for elem in ans:
    print(elem)