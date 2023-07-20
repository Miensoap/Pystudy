n=int(input())
arr=list(input())
ans=0
for i in range(n):
    tarr=arr[:]
    mindis=21
    if tarr[i]=='0':
        tarr[i]='1'
    else:
        continue

    for j in range(n):
        if tarr[j]=='1':
            for k in range(j+1,n):
                if tarr[k]=='1':
                    dis=k-j
                    mindis=min(dis,mindis)
                    break
    ans=max(mindis,ans)

print(ans)
