def min_gbs(n,m):
    a=n*m
    c=min(n,m)
    for i in range(a+1,c,-1):
        if i%n ==0 and i%m ==0:
            b=i
    print(b)

n,m=tuple(map(int,input().split()))
min_gbs(n,m)
