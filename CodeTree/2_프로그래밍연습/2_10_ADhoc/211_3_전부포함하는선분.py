n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
ans=101

for i in range(n):
    maxx=0
    minx=101
    for j in range(n):
        if j==i:
            continue
        maxx=max(maxx,arr[j][1])
        minx=min(minx,arr[j][0])
    
    lenth=maxx-minx
    ans=min(lenth,ans)

print(ans)

# 5
# 15 53
# 3 88
# 15 85
# 40 90
# 4 50