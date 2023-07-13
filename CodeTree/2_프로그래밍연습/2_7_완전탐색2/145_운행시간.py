import sys
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
sche = [0]*1000

for elem in arr:
    for i in range(elem[0],elem[1]):
        sche[i-1]+=1

ans=0
for elem1 in arr:
    cnt=0
    for elem2 in arr:
        if elem1==elem2:
            for i in range(elem1[0],elem1[1]):
                sche[i-1]-=1
        
    for j in sche:
        if j>=1:
            cnt+=1

    ans=max(ans,cnt)

    for i in range(elem1[0],elem1[1]):
        sche[i-1]+=1

print(ans)

