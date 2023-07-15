n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
cnt=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            narr=[0]*101
            for l in range(n):
                if l==i or l==j or l==k:
                    continue
                elem=arr[l]
                for m in range(elem[0],elem[1]+1):
                    narr[m]+=1
            
            max_narr=max(narr)
            if max_narr<2:
                cnt+=1

print(cnt)
