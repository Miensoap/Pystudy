x,y=map(int,input().split())
ans=0

for i in range(x,y+1):
    arr=list(map(int,list(str(i))))
    su=sum(arr)
    ans=max(su,ans)

print(ans)