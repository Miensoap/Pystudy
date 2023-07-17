n,c,g,h=map(int,input().split())
arr=[tuple(map(int,input().split())) for _ in range(n)]

st=sorted(arr,key=lambda x : x[0])[0][0]
end=sorted(arr,key=lambda x : x[1], reverse=True)[0][1]

ans=0
for i in range(st,end+1):
    cnt=0
    for elem in arr:
        if i<elem[0] : 
            cnt+=c
        elif i>elem[1]:
            cnt+=h
        else:
            cnt+=g
    ans=max(ans,cnt)

print(ans)
