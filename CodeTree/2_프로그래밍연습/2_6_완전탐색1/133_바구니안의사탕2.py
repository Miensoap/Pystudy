n,k=map(int,input().split())
arr=[0]*500
for i in range(n):
    temp=list(map(int,input().split()))
    arr[300+temp[1]-1]+=temp[0]

max_val=0
for i in range(300-k,500-k):
    sum=0
    for j in range(i-k,i+k+1):
        sum+=arr[j]
    max_val=max(max_val,sum)

print(max_val)