def printl(n):
    if n == 0:        
        return
    if n==1:
        print(n)  
    else:
        print(n,end=' ')
    printl(n-1)

def printf(n):
    global a
    if n == 0:        
        return 
    printf(n-1)
    if n==a:
        print(n) 
    else :
        print(n,end=' ')

a=int(input())
printf(a)
printl(a)
    