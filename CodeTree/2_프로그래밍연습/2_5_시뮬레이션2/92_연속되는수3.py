cnt = 0
ans = 0
n=int(input())
arr=[int(input()) for _ in range(n)]

for i in range(len(arr)):
    cnt +=1
    if cnt>=ans:
        ans=cnt
    if arr[i]*arr[i - 1]<0:
        cnt =0

print(ans)