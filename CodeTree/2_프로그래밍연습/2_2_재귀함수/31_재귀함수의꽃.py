def printn(n):
    if n==0:
        return
    print(n,end=' ')
    printn(n-1)
    print(n,end=' ')

printn(int(input()))