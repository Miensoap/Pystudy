a=list(map(int,input().split()))
b=1
c=0
for i in range(len(a)):
    b*=a[i]
# print(b)
def bsh(b):
    global c
    c+=b%10
    if b==0:
        return c
    return bsh(b//10)
           
print(bsh(b))
