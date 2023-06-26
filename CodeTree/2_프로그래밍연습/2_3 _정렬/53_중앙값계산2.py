n=int(input())
arr=list(map(int,input().split()))
mrr=[]
for i in range(len(arr)):
    mrr.append(arr[i])
    mrr.sort()
    if i==0 or i%2==0:
        print(mrr[(len(mrr))//2],end=' ')
        #sorted : iterable