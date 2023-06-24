def fil(n):
    for i in range(2,n):
        if n%i==0:
            return(False)
            break
    if (n%10 + n//10 + n//100)%2 !=0:
        return(False)    
    
    return(True)

a,b=map(int,input().split()) 
cnt=0
for i in range(a,b+1):
    if fil(i):
        cnt+=1

print(cnt)