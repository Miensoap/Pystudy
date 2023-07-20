n,m=map(int,input().split())
segments=[sorted(tuple(map(int,input().split()))) for _ in range(m)]

max_cnt = 0
for i in range(m):
    cnt=segments.count(segments[i])
    max_cnt = max(max_cnt, cnt)

print(max_cnt)