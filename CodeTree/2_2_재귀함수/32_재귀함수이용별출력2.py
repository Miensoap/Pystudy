def prints(n):
    if n==0:
        return
    print('* '*n)
    # print('\n')
    prints(n-1)
    print('* '*n)
    # print('\n')

prints(int(input()))