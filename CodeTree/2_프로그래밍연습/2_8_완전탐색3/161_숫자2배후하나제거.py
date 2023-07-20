import sys
n=int(input())
arr=list(map(int,input().split()))
ans=sys.maxsize

for i in range(n):
    tarr=arr[:]
    tarr[i]*=2
    for j in range(n):
        jarr=[]
        for k,elem in enumerate(tarr):
            if k!=j:
                jarr.append(elem)
            a=0
        for k in range(n-2):
            a+=abs(jarr[k+1]-jarr[k])

        ans=min(ans,a)

print(ans)

         