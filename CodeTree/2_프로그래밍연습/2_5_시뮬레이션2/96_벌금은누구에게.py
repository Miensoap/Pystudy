n,m,k=map(int,input().split())
cnt=[0 for _ in range(n)]
fan=[int(input()) for _ in range(m)]
ans=-1
for elem in fan:
    cnt[elem-1]+=1
    if cnt[elem-1]>=k:
        ans=elem
        break

print(ans)


