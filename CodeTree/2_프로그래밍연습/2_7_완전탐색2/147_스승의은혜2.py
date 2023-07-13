def isok(a,b):
    if a>=b:
        return True
    else:
        return False
    
n,b=map(int,input().split())
p=[int(input())for _ in range(n)]

ans=0

for i in range(n):
    pi=p[:]
    pi[i]//=2
    pi.sort()
    b1=b
    cnt=0
    # print(pi)

    for elem in pi:
        if isok(b1,elem):
            cnt+=1
            b1-=elem
        else:
            break
    
    ans=max(cnt,ans)

print(ans)
