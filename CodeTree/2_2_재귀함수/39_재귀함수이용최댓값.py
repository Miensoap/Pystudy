# def chd(n,a):
#     if n==0:
#         return(n+1)
#     b=a[n-1]
#     if chd(n-1,a)>b:
#         return chd(n-1,a)
#     return b

n=int(input())
a=list(map(int,input().split()))

def chd(n):
    if n == 0:
        return a[0]
    return max(chd(n - 1), a[n])

print(chd(n-1))