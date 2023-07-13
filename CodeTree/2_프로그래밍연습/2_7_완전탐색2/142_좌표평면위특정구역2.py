import sys
n = int(input())
segments = [list(map(int,input().split())) for _ in range(n)]

ans = sys.maxsize
for i in range(n):
    maxx,maxy=0,0
    minx,miny=40001,40001
    for j in range(n):
        if j == i:
            continue
        x, y = segments[j][0],segments[j][1]
        maxx,maxy=max(maxx,x),max(maxy,y)
        minx,miny=min(minx,x),min(miny,y)
        rec=(maxx-minx)*(maxy-miny)

    ans = min(ans, rec)

print(ans)