n,L=map(int,input().split())
arr=list(map(int,input().split()))
ans=0

for h in range(100):
    tarr=[x for x in arr if x>=h-1]
    h1_cnt=tarr.count(h-1)
    if h1_cnt<=L: #다올릴수있음
        h_cnt=len(tarr)
    else:
        h_cnt=len(tarr)-(h1_cnt-L) #못올리는개수 뺌
    
    if h<=h_cnt:
        score=h
        ans=max(score,ans)
    else:
        continue

print(ans)
    