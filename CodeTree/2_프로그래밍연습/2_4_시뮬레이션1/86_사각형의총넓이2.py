n=int(input())
# x1,y1,x2,y2=map(int,input().split())
# a1,b1,a2,b2=map(int,input().split())
offset=1001
rows=2001
cols=2001
arr=[[0 for j in range(cols)] for i in range(rows)]

def chil(x1,y1,x2,y2):
    global offset
    for i in range(x1+offset,x2+offset):
        for j in range(y1+offset,y2+offset):
            arr[i][j]=1

# chil(x1,y1,x2,y2)
# chil(a1,b1,a2,b2)

for i in range(n):
   chil(*map(int,input().split()))


sum=0
for i in range(rows):
    for j in range(cols):
        if arr[i][j]==1:
            sum+=1
print(sum)