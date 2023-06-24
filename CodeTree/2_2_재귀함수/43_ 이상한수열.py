n=int(input())
def ns(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return ns(n//3)+ns(n-1)
print(ns(n))