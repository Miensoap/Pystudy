def move(x,y,dir_num):
    dx,dy = [0,1,-1,0],[1,0,0,-1]
    nx,ny= x+dx[dir_num],y+dy[dir_num]
    return nx,ny

def in_range(nx,ny,n):
    return 0<=nx<n and 0<=ny<n

x,y=1000,1000
n=int(input())
nmove=[tuple(input().split()) for _ in  range(n)]
arr1=[['o' for _ in range(n)] for _ in range(2000)]

dir={'E':1,'W':2,'N':3,'S':0}
cnt=0
for elem in nmove:
    if cnt !=0 and x==1000 and y==1000 :
            break
    for i in range(int(elem[1])):
        cnt+=1
        x,y = move(x,y,dir[elem[0]])
        if x==1000 and y==1000 :
            break

if  x!=1000 or y!=1000 : 
    print(-1)
else:
    print(cnt)



    


