import sys
def dist(arr):
    dis=0
    for i in range(1,len(arr)):
        dis+=abs(arr[i-1][0]-arr[i][0])+ abs(arr[i-1][1]-arr[i][1])

    return dis

n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
min1=sys.maxsize

for i in range(1,n-1):
    narr=arr[:]
    narr.remove(narr[i])
    dis=dist(narr)

    min1=min(min1,dis)

print(min1)


