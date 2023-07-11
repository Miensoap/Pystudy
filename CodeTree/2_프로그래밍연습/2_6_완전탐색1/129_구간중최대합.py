n,k=map(int,input().split())
arr = list(map(int,input().split()))
ans=0
for i in range(n - k + 1):
    sum=0
    for j in range(i, i + k):
        sum+=arr[j]

    ans=max(ans,sum)
print(ans)