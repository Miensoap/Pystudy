def ver_carry(a,b,c):
    # 각 자리끼리 더해서 10이넘는게있으면 False
    arr=[a,b,c]
    narr=[[],[],[],[],[]]
    maxn=0
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
    
    for elem in narr:
        maxn=max(maxn,sum(elem))
    
    if maxn>=10:
        return False
    else:    
        return True

def ver_max(arr):
    maxn=-1
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                a,b,c=arr[i],arr[j],arr[k]
                if ver_carry(a,b,c):
                   maxn=max(maxn,a+b+c)
    return maxn

n=int(input())
arr=[int(input()) for _ in range(n)]
# print(arr)
print(ver_max(arr))



