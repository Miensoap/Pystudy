import sys
n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]

for i in range(1,100):
    its=False
    for elem in arr:
        if not elem[0]<=i<=elem[1]:
            its=False
            break
        else:
            its=True
    if its:
        print("Yes")
        sys.exit()
print("No")

