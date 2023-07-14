k,n=map(int,input().split())
arr=[tuple(map(int,input().split())) for _ in range(k)]

ans=[set() for _ in range(k)]


for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for l in range(k):
            if arr[l].index(i+1)<arr[l].index(j+1) :
                ans[l].add((i+1,j+1))


for i in range(len(ans)-1):
    ans[i+1] = ans[i].intersection(ans[i+1])

print(len(ans[k-1]))
    
         
