# 3=12 4=23 5=34 6=45 ... n=n-2 n-1
def pibo(n):
    if n==2 or n==1:
        return 1
    return pibo(n-1)+pibo(n-2)

print(pibo(int(input())))

# def trif(n, k):
#     if n <= k:
#         return n
#     return trif(n - 1, k) + trif(n - 2, k) + trif(n - 3, k)

# print(trif(8,4))

