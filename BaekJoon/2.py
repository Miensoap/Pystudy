import collections

def move1(x,y,dir_num):
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    nx,ny=x+dx[dir_num],y+dy[dir_num]
    return nx,ny

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False
        
def ch_dis(a,b):
    queue=collections.deque()
    for i in range(4):
        x,y=move1(a,b,i)
        if in_range(x,y):
            queue.put()

n,m=map(int,input().split())
arr=[list(input())for _ in range(n)]

for i in range(m+1):
    do_ch=0
    for j in range(n):
        for k in range()