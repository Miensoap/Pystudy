n=int(input())
arr = list(map(int,input().split()))

cnt=0
for i in range(n):
    for j in range(i, n):
        sum=0
        for k in range(i, j + 1):
            sum+=arr[k]
            avg=sum/(j-i+1)
        
        for k in range(i, j + 1):
            if avg==arr[k]:
                cnt+=1
                break

print(cnt)