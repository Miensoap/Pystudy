n=int(input())
offset=100
rows=200
cols=200
arr=[[0 for j in range(cols)] for i in range(rows)]

def chil(x1,y1):
    global offset
    for i in range(x1+offset,x1+8+offset):
        for j in range(y1+offset,y1+8+offset):
            arr[i][j]=1

for i in range(n):
   chil(*map(int,input().split()))

sum=0
for i in range(rows):
    for j in range(cols):
        if arr[i][j]==1:
            sum+=1
print(sum)



            