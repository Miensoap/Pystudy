def two(n,m):
    if n>m:
        n+=25
        m*=2
    else:
        n*=2
        m+=25
    
    return n,m

a,b=map(int,input().split())
for elem in two(a,b):
    print(elem,end=' ')