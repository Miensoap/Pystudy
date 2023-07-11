n,m=map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt=0
for i in range(n-m+1):
    ok=0
    temp=[]
    for j in range(i, i+m):
        temp.append(a[j])
    for elem in b:
        if not elem in temp:
           break
        ok+=1
        temp.remove(elem)                
                
    if ok==m:
        cnt+=1


print(cnt)