import sys
def move(x,y):
    global dir_num
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    nx,ny= x+dx[dir_num],y+dy[dir_num]
    
    if in_range(nx,ny,n):
        return nx,ny

def in_range(nx,ny,n):
    return 0<=nx<n and 0<=ny<n

def rotate(D):
    global dir_num
    if D=='R':
        dir_num = (dir_num + 1) % 4
    elif D=='L':
        dir_num = (dir_num+3)%4


n=1000
x,y=n//2 , n//2
nmove=arr1=list(sys.stdin.readline().rstrip())
# print(nmove)
arr1=[[' ' for _ in range(n)] for _ in range(n)]
# print(arr1)
dir_num=3

cnt=0
for elem in nmove:
    if cnt !=0 and x==2//n and y==2//n :
            break
    
    if elem == 'F':
        cnt+=1
        x,y = move(x,y)
        if x==n//2 and y==n//2 :
            break
    else : 
        cnt+=1
        rotate(elem)


if  x!=n//2 or y!=n//2 : 
    print(-1)
else:
    print(cnt)







    


