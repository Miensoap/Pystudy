offset=1000
rows=2000
cols=2000
arr=[[0 for j in range(cols)] for i in range(rows)]

def chil(x1,y1,x2,y2):
    global offset
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]=1

def chil2(x1,y1,x2,y2):
    global offset
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]=2

chil(*map(int,input().split()))
chil2(*map(int,input().split()))

irr=set()
jrr=set()
for i in range(rows):
    for j in range(cols):
        if arr[i][j]==1:
            irr.add(i)
            jrr.add(j)
if len(irr)==0 or len(jrr)==0:
    hei,bro=0,0
else:
    hei=(max(irr)-min(irr))+1
    bro=(max(jrr)-min(jrr))+1

print(hei*bro)            