def div(x,y,arr):
    div1=[]
    div2=[]
    div3=[]
    div4=[]
    for elem in arr:
        if elem[0]>x and elem[1]>y:
            div1.append(elem)
        elif elem[0]>x and elem[1]<y:
            div2.append(elem)
        elif elem[0]<x and elem[1]<y:
            div3.append(elem)
        elif elem[0]<x and elem[1]>y:
            div4.append(elem)
    
    return len(div1),len(div2),len(div3),len(div4)

n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
ans=100

for i in range(0,101,2):
    for j in range(0,101,2):
        div1,div2,div3,div4 = div(i,j,arr)
        maxlen=max(div1,div2,div3,div4)
        ans=min(ans,maxlen)

print(ans)


