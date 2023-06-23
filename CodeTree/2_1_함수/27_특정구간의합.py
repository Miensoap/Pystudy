n,m=map(int,input().split())
a=list(map(int,input().split()))

def tgh(a,m):
    sum=0
    # c=[]
    # for i in range(m):
    #     b=tuple(map(int,input().split()))
    #     c.append(b)
    c=[tuple(map(int,input().split())) for _ in range(m)]
    
    for i in range(len(c)):
        a1,a2=c[i][0],c[i][1]
        for j in range(a1-1,a2) :
            sum+=a[j]
        print(sum)
        sum=0
    
tgh(a,m)
