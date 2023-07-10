def gong_goo(n):
    if n==1:
        return arr[0]
    
    k=arr[n-1]
    l=gong_goo(n-1)

    for i in range(2, k*l +1):
        if i % k == 0 and i % l == 0:
            return i
    
n=int(input())
arr=list(map(int,input().split()))
print(gong_goo(n))  