import collections

def move(a,b,num):
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    nx,ny=a+dx[num],b+dy[num]
    return nx,ny

def in_range(nx,ny):
    return 0<=nx<n and 0<=ny<n


n,l,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
day_cnt=0
visited=[[False] * n for _ in range(n)]

def union(now:list):
    union_col=[]
    queue=collections.deque()
    queue.append(now)
    sumu=0
    su=0
    while queue:
        now=queue.popleft()
        # if visited[now[0]][now[1]]:
        #     continue
        visited[now[0]][now[1]] = True
        sumu+=arr[now[0]][now[1]]
        su+=1
        for i in range(4):
            visit=move(now[0],now[1],i)
            if in_range(visit[0],visit[1]) and not visited[visit[0]][visit[1]] and l <= abs(arr[visit[0]][visit[1]]-arr[now[0]][now[1]]) <= r:
                queue.append(visit)
                union_col.append(visit)
                visited[visit[0]][visit[1]] = True
    
    if su>1:
        return sumu//su , union_col
    else:
        return -1,[]
 

cnt=0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue  
        union_user,union_col=union([i,j])[0]
        # union_col=union([i,j])[1]
        if union_user >0:
            for elem in union_col:
                arr[elem[0]][elem[1]]=union_user
            cnt+=1

print(cnt)
                
            

                 

            





    
    

