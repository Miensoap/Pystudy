import sys

n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=sys.maxsize

for i in range(10000):
    cost=0
    for j in range(n):
        if arr[j]<i:
            cost+=abs(arr[j]-i)
        if arr[j]>i+k:
            cost+=abs(arr[j]-i-k)
    
    ans=min(ans,cost)

print(ans)