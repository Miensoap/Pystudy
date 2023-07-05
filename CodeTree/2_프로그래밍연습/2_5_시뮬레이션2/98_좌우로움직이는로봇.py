n,m=map(int,input().split())
nmove=[tuple(input().split()) for _ in  range(n)]
mmove=[tuple(input().split()) for _ in  range(m)]

arrn = []
arrm = []
first = []

minarr=[]
maxarr=[]

def move(arr,oarr):
    now=500000
    for i in range(len(arr)):
        d = int(arr[i][0])
        if arr[i][1] == 'R':
            for i in range(1, d+1):
                now += 1
                oarr.append(now)
        elif arr[i][1] =='L':
            for i in range(1,d+1):
                now -= 1
                oarr.append(now)

move(nmove,arrn)
move(mmove,arrm)

if len(arrn)<=len(arrm):
    minarr,maxarr=arrn,arrm
else:
    minarr,maxarr=arrm,arrn

for i in range(len(maxarr)-len(minarr)): 
    minarr.append(minarr[len(minarr)-1])

cnt=0
on=0
for i in range(len(maxarr)):
    if maxarr[i]==minarr[i]:
        if on==1 :
            cnt+=1
        on=0
    else:
        on=1

print(cnt)

    


