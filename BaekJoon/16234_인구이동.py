from collections import deque
import math

def move(a,b,num):
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    nx,ny=a+dx[num],b+dy[num]
    return nx,ny

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n


n,l,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
day_cnt=0


def union(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    count = arr[i][j]  

    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx,ny=move(x,y,d)

            if not in_range(nx,ny):
                continue
            if visit[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r: 
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += arr[nx][ny]
    for x, y in union:
        arr[x][y] = math.floor(count /len(union) )

    return len(union)
 

cnt=0
while True:
    visit=[[False] * n for _ in range(n)]
    flag=False
    
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if union(i,j)>1:
                    flag=True
    
    if not flag:
        break
    cnt+=1

print(cnt)

                
            

                 

            





    
    

