n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a=arr[n]
for i in range(n):
    if (arr[i+n]-arr[i])<a:
        a=(arr[i+n]-arr[i])

print(a)