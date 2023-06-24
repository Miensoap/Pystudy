n=int(input())
def ns(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return ns(n-1)*ns(n-2)%100
print(ns(n))