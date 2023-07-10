n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        if max_cnt <=arr[i][j] + arr[i][j+1] + arr[i][j + 2]:
            max_cnt = arr[i][j] + arr[i][j+1] + arr[i][j + 2]
            tmp=(i,j)
max_cnt2=0
for i in range(n):
    for j in range(n - 2):
        if i!=tmp[0] or (tmp[1]>j+2 or j>tmp[1]+2) :
            max_cnt2 = max(max_cnt2, arr[i][j] + arr[i][j+1] + arr[i][j + 2])

print(max_cnt+max_cnt2)