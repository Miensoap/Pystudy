def hj(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return n+hj(n-2)

print(hj(int(input())))