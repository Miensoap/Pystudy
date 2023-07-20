n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
ans=[]

for i in range(3):
    score=0
    zo=[0,0,0]
    zo[i]=1
    for elem in arr:
        tmp=zo[elem[0]-1]
        zo[elem[0]-1]=zo[elem[1]-1]
        zo[elem[1]-1]=tmp
    
        if zo[elem[2]-1]==1:
            score+=1
    ans.append(score)

maxs=max(ans)
# print(ans.index(maxs)+1)  
print(maxs)




