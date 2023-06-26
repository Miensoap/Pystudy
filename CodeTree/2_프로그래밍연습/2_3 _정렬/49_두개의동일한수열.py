n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
if sorted(arr1)==sorted(arr2):
    print('Yes')
else:
    print('No')