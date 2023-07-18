def pn(j):
    return(tarr[j]>0)

n=int(input())
arr=[int(input()) for _ in range(n)]
ans=0

for i in range(min(arr),max(arr)):
    tarr=arr[:]
    for j in range(n):
        tarr[j]-=i

    if pn(0):
        cnt=1
    else:
        cnt=0
        
    for j in range(1,n): 
        if pn(j)!=pn(j-1) and pn(j) :
            cnt+=1
    ans=max(ans,cnt)

print(ans)
