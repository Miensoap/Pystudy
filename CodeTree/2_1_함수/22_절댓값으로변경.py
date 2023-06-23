n=int(input())
arr=list(map(int,input().split()))

def absd(a):
    for i in range(0,n):
        # if a[i]<0:
        #     a[i]*=-1
        a[i]=abs(a[i])

    return(a)
    
for elem in absd(arr):
    print(elem,end=' ')
