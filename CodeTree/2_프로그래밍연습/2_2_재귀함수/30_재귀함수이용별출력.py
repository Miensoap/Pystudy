def prints(n):
    if n==0:
        return
    prints(n-1)
    print('*'*n)

prints(int(input()))