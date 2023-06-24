def two(n,m):
    if n>m:
        n*=2
        m+=10
    else:
        n+=10
        m*=2
    
    return n,m

a,b=map(int,input().split())
for elem in two(a,b):
    print(elem,end=' ')