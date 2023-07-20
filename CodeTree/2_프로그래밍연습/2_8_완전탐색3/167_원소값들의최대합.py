n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=0

for s in range(n):#시작위치
    cnt=0
    loc=arr[s]
    for i in range(m):#반복
        cnt+=loc
        loc=arr[loc-1]
    
    ans=max(ans,cnt)

print(ans)

