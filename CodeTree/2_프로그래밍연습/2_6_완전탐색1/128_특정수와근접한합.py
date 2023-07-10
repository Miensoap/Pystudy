import sys
n,s=map(int,input().split())
arr=list(map(int,input().split()))
mini=sys.maxsize
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        num=sum(arr)-arr[i]-arr[j]
        if mini>abs(s-num):
            mini=abs(s-num)
            # ans=(i,j)

print(mini)