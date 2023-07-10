import sys
def dist(arr,i):
    dis=0
    for j in range(len(arr)):
        if j>=i:
            dis+=abs(i-j)*arr[j]
        else:
            dis+=(len(arr)-(i-j))*arr[j]
    return dis

n=int(input())
arr=[int(input())for _ in range(n)]
min1=sys.maxsize

for i in range(n):
    dis=dist(arr,i)
    min1=min(min1,dis)

print(min1)


