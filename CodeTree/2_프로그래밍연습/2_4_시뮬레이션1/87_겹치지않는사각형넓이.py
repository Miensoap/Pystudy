n=2
offset=1001
rows=2001
cols=2001
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

for i in range(n):
   chil(*map(int,input().split()))
chil2(*map(int,input().split()))

# irr=[]
# jrr=[]
# for i in range(rows):
#     for j in range(cols):
#         if arr[i][j]==1:
#             irr.append(i)
#             jrr.append(j)

# hei=(max(irr)-min(irr))
# bro=(max(jrr)-min(jrr))
# print(hei*bro)

sum=0
for i in range(rows):
    for j in range(cols):
        if arr[i][j]==1:
            sum+=1
print(sum)



            