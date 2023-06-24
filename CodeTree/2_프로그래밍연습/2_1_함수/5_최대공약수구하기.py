def max_gys(n,m):
    a=min(n,m)
    for i in range(1,a+1):
        if n%i ==0 and m%i ==0:
            b=i
    print(b)

n,m=tuple(map(int,input().split()))
max_gys(n,m)



