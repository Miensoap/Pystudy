n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for elem in arr:
    print(elem,end=' ')
print('\n',end='')
arr.sort(reverse=True)
for elem in arr:
    print(elem,end=' ')