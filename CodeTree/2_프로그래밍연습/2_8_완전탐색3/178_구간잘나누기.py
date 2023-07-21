n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans=10001

for maxsum in range(max(arr),sum(arr)):#최댓값
    section=1
    vals=[]
    for j in range(n):
        if sum(vals)+arr[j]<=maxsum:
            vals.append(arr[j])
        else:
            section+=1
            vals=[arr[j]]
            
    if section<=m and sum(vals)<=maxsum:
        ans=min(ans,maxsum)
        break

print(ans)