from itertools import combinations
import sys

def ch_dis(a,b,com):
    min_dis=sys.maxsize
    for elem in com:
        dis=abs(a-elem[0])+abs(b-elem[1])
        min_dis=min(dis,min_dis)
    
    return min_dis


n,m=map(int,input().split())
arr=[list(input().split())for _ in range(n)]
chz=[]
ans=sys.maxsize

for i in range(n):
    for j in range(n):
        if arr[i][j]=='2':
            chz.append((i,j))

combi = list(combinations(chz,m))

for com in combi:
    do_ch=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='1':
                do_ch+=ch_dis(i,j,com)
    ans=min(ans,do_ch)
    
print(ans)

    
