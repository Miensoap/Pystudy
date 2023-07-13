n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort(key= lambda x : x[0])
# print(arr)
cnt=0

for i in range(n):
    ok=True
    for j in range(n):
        if i==j:
            continue
        
        if arr[i][0]>arr[j][0] and arr[j][1]>arr[i][1]:
            ok=False
            break
        elif arr[i][0]<arr[j][0] and arr[i][1]>arr[j][1]:
            ok=False
            break
        ok=True
 
    if ok : 
        cnt+=1

print(cnt)
