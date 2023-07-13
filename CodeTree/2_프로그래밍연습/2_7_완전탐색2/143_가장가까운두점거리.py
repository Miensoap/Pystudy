import sys
n = int(input())
segments = [list(map(int,input().split())) for _ in range(n)]

ans = 1000*1000
for i in range(n):
    for j in range(n):
        if j == i:
            continue    
        x1, y1 = segments[i]
        x2, y2 = segments[j]

        dis = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
        ans = min(ans, dis)

print(ans)