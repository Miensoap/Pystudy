import sys
n=int(input())
arr=list(map(int,input().split()))
ans=sys.maxsize
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        sum+=abs(i-j)*arr[j]
    if sum<=ans :
        ans=sum

print(ans)
