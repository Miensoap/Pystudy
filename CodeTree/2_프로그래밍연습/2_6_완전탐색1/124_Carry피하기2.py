n=int(input())
arr=[int(input()) for _ in range(n)]
# print(arr)

narr=[[],[],[],[],[]]
# arr1=[]
# arr10=[]
# arr100=[]
# arr1000=[]
# arr10000=[]
ans=[]

for elem in arr:
    narr[0].append(elem%10)
    elem=elem//10
    narr[1].append(elem%10)
    elem=elem//10
    narr[2].append(elem%10)
    elem=elem//10
    narr[3].append(elem%10)
    elem=elem//10
    narr[4].append(elem%10)

def ver_max(arr):
    maxn=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if j!=i!=k:
                    maxn=max(maxn,arr[i]+arr[j]+arr[k])
    return maxn

for elem in narr:
    temp=0
    temp=ver_max(elem)
    if temp<10:
        ans.append(elem)


if elem in ans:
    print(max(ans))
else:
    print(-1)

