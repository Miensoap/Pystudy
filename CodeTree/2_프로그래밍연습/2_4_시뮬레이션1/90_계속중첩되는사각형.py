n=int(input())
offset=100
rows=200
cols=200
arr=[['i' for j in range(cols)] for i in range(rows)]

def chil(x1,y1,x2,y2):
    global offset
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]='R'

def chil2(x1,y1,x2,y2):
    global offset
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]='B'

for i in range(n):
   if i%2==0:
    chil(*map(int,input().split()))
   else:
    chil2(*map(int,input().split()))

sum=0
for i in range(rows):
    for j in range(cols):
        if arr[i][j]=='B':
            sum+=1
print(sum)



            