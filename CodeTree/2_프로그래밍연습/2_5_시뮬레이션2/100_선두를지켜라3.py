n,m=map(int,input().split())
nmove=[tuple(input().split()) for _ in  range(n)]
mmove=[tuple(input().split()) for _ in  range(m)]

arrn = []
arrm = []
first = []

minarr=[]
maxarr=[]
minsym='i'
maxsym='i'

def move(arr,oarr):
    now=0
    for i in range(len(arr)):
        v=int(arr[i][0])
        t=int(arr[i][1])
        if v >0:
            for i in range(1, 1+v*t,v):
                now += v
                oarr.append(now)
        else : 
            for i in range(t):
                now+=v
                oarr.append(now)

move(nmove,arrn)
move(mmove,arrm)

if len(arrn)<=len(arrm):
    minarr,maxarr=arrn,arrm
    minsym,maxsym='n','m'
else:
    minarr,maxarr=arrm,arrn
    minsym,maxsym='m','n'

for i in range(len(maxarr)-len(minarr)): 
    minarr.append(minarr[len(minarr)-1])

for i in range(len(maxarr)):
    if maxarr[i]>minarr[i]:
        first.append(maxsym)
    elif minarr[i]>maxarr[i]:
        first.append(minsym)
    else:
        first.append((maxsym,minsym))

cnt=0
for i in range(len(first)):
    if i!=0 and first[i]!=first[i-1]:
        cnt+=1

print(cnt+1)

    


