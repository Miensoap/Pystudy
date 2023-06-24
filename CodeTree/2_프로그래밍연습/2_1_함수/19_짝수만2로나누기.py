n=int(input())
arr=list(map(int,input().split()))

def jak(a):
    for i in range(len(a)):
        if a[i]%2==0:
            a[i]//=2

jak(arr)
for elem in arr:
    print(elem, end=' ')