def fact(n):
    if n == 0:
        return 0

    return fact(n//10) + (n%10)**2


print(fact(int(input())))