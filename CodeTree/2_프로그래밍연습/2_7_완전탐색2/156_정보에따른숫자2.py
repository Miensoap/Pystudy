T,a,b=map(int,input().split())
# minx=1001
# maxx=0

arr=[0]*1001
for i in range(T):
    c,x=input().split()
    # minx=min(int(x),minx)
    # maxx=max(int(x),maxx)
    arr[int(x)]=c

cnt=0
for i in range(a,b+1):
    dis_s=0
    dis_n=0

    j,k=i,i
    while arr[j]!='S' and arr[k]!='S':
        if j==b and k==a:
            break
        if j<b:
            j+=1
        if k>a:
            k-=1
        
        dis_s+=1
    
    j,k=i,i
    while arr[j]!='N' and arr[k]!='N':
        if j==b and k==a:
            break
        if j<b:
            j+=1
        if k>a:
            k-=1
        
        dis_n+=1
    
    if dis_s<=dis_n:
        cnt+=1

print(cnt)


