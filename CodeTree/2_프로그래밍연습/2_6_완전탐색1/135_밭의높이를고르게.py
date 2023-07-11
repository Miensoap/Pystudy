n,h,t=map(int,input().split())
arr=list(map(int,input().split()))
mincnt=10000000

for i in range(n-t+1):
    cnt=0
    for j in range(i,i+t):
        cnt+=abs(arr[j]-h) 
    
    mincnt=min(mincnt,cnt)

print(mincnt)
