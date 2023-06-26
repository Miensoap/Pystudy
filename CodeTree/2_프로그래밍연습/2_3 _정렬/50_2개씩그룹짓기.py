n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a=0
for i in range(n):
    if (arr[i]+arr[2*n-1-i])>a:
        a=(arr[i]+arr[2*n-1-i])

print(a)