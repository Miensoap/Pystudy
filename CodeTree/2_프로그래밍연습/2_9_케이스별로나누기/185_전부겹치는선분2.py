import sys
n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]

for i in range(1,100):
    its=False
    for j in range(n):
        for k in range(n):
            if j==k:
                continue
            if not arr[k][0]<=i<=arr[k][1]:
                its=False
                break
            else:
                its=True
        if its:
            print("Yes")
            sys.exit()
print("No")

