n=3
arr=[list(input()) for _ in range(n)]
ans=[]
cnt=0

for i in range(n): # 00 01 02, 10 11 22 ,20 21 22
    temp1=set()
    temp2=set()
    for j in range(n):
        temp1.add(arr[j][i])
        temp2.add(arr[i][j])
    ans.append(temp1)
    ans.append(temp2)

temp=set()
for i in range(n): #00, 11, 22
    temp.add(arr[i][i])
ans.append(temp)

temp=set()
# for i in range(n): # 02 11 20
#     temp.add(arr[i][[n-1-i]])
temp.add(arr[0][2])
temp.add(arr[1][1])
temp.add(arr[2][0])
ans.append(temp)

comp=ans[:]

for elem in ans:
    if len(elem)==2 and elem in comp:
        cnt+=1
        # for i in comp:
        #     if i==elem:
        #         comp.remove(i)
        comp=[i for i in comp if i!=elem]  # list comprehension


print(cnt)

