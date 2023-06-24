n,m=map(int,input().split())
a=list(map(int,input().split()))

def nbh(a,m):
    sum=0
    while True:
        sum+=a[m-1]
        if m==1:
            break
        if m%2==1:
            m-=1
        else:
            m//=2
        
    return(sum)

print(nbh(a,m))