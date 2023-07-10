n=int(input())
arr=list(map(int,input().split()))
maxnum=0
for i in range(len(arr)-2):
    for j in range(i+2,len(arr)):
        num=arr[i]+arr[j]
        maxnum=max(maxnum,num)

print(maxnum)