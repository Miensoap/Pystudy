def isok(a,b):
    if a>=b:
        return True
    else:
        return False
    
n,b=map(int,input().split())
p=[list(map(int,input().split()))for _ in range(n)]

ans=0

for i in range(n):
    pi=[p[i][:] for i in range(n)]
    pi[i][0]//=2
    pi.sort(key= lambda x : x[0]+x[1])
    b1=b
    cnt=0
    # print(pi)

    for elem in pi:
        sum=elem[0]+elem[1]
        if isok(b1,sum):
            cnt+=1
            b1-=sum
        else:
            break
    
    ans=max(cnt,ans)

print(ans)
