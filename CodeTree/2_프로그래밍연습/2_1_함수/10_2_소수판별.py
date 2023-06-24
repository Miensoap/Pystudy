def sosu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a,b=map(int,input().split())
c=0

for i in range(a,b+1):
    if sosu(i):
        c+=i

print(c)