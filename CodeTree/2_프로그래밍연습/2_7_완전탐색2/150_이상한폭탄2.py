n,k=map(int,input().split())
arr=[int(input())for _ in range(n)]
bom=[]

if k==n:
    for i in range(1):
        for j in range(1,n): 
            if arr[i]==arr[j]:
                bom.append(arr[i])
    
    
for i in range(n-k): #0  24
    for j in range(i+1,i+k+1): # 1~40  25~64
        if arr[i]==arr[j]:
            bom.append(arr[i])

for i in range(n-1,k-1,-1): 
    for j in range(i-1,i-k-1,-1): 
        if arr[i]==arr[j]:
            bom.append(arr[i])

if len(bom)>0:
    print(max(bom))
else:
    print(-1)
     
