import sys
n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]

for i in range(1,10000):
    num=i
    flag=False
    for j in range(n):
        num*=2
        a,b=arr[j]
        if not a<=num<=b :
            flag=True
            break
    if flag : continue
    print(i)
    sys.exit()



