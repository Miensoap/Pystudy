def onj(n):
    if n%2!=0:
        if n%10!=5:
            if (n%3==0 and n%9!=0)==False:
                return(True)
            else:
                return(False)
        else:
            return(False) 
    else:
        return(False)    

a,b=map(int,input().split()) 
cnt=0
for i in range(a,b+1):
    if onj(i):
        cnt+=1

print(cnt)
            
