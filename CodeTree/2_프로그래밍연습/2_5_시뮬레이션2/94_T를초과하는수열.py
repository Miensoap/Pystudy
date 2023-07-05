cnt = 0
ans = 0
n,T=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    cnt +=1
    if arr[i]<=T:
        cnt =0
    if cnt>=ans:
        ans=cnt
    

print(ans)