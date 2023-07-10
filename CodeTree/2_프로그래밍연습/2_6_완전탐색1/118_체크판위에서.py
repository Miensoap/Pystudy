n,m = map(int,input().split())
arr = [list(input().split()) for _ in range(n)]
cnt = 0
for i in range(1,n):
    for j in range(1,m):
        if arr[i][j]!=arr[0][0]:
            for k in range(i+1,n-1):
                for l in range(j+1,m-1):
                    if arr[k][l]!=arr[i][j]:
                        cnt+=1

if arr[n-1][m-1]==arr[0][0]:
    cnt=0

print(cnt)