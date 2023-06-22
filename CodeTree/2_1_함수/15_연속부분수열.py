def ybs(n,m):
    #t없을때 UnboundLocalError: local variable 't' referenced before assignment
    t=0
    for i in range(len(n)):
        if n[i]==m[0] :
            t=i
            break       
    for j in range(len(m)):
        if n[t+j]!=m[j]:
            return 'No'
    return 'Yes'

a,b=map(int,input().split())
ar=list(map(int,input().split()))
br=list(map(int,input().split()))

if a>=b:
    n=ar
    m=br
else:
    n=br
    m=ar

print(ybs(n,m))