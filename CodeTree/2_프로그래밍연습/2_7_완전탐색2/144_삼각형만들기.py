n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
def b(i,j,k):
    return abs( (i[0]*j[1]+j[0]*k[1]+k[0]*i[1]) - (i[1]*j[0]+j[1]*k[0]+k[1]*i[0]) )
    

ans = 0
for i  in arr:
    for j in arr:
        if i==j or i[0]!=j[0]: 
            continue
        for k in arr:
            if k==i or k==j :
                continue
            if k[1]==i[1] or k[1]==j[1]:
                max_b = b(i, j, k)
                ans = max(ans, max_b)

print(ans)