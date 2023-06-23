def fact(n):
    if n == 1:
        return 0
    cnt=0
    if n%2==0:
        m=n//2
    else:
        m=n//3
    cnt+=1
    return fact(m) + cnt

print(fact(int(input())))