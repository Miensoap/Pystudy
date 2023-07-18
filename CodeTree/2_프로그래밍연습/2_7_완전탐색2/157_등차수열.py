n=int(input())
arr=list(map(int,input().split()))

ans=0
for k in range(1,101):
    cnt=0
    for i in range(1,100):
        if k-i in arr and k+i in arr:
            cnt+=1
    ans=max(cnt,ans)

print(ans)
# print(sorted(arr))
