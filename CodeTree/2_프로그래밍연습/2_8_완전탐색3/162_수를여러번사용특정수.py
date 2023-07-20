import sys
a,b,c=map(int,input().split())
n,m=c//a,c//b
ans=0

for i in range(n+1):
    for j in range(m+1):
        k=(i)*a
        k+=(b*j)

        if k<=c:
            ans=max(ans,k)
        else:
            break

print(ans)