def ver_dis(a,b):
    if abs(a-b)<=2 or abs(a-b)>=n-2:
        return True    
    else:
        return False

n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if (ver_dis(i,arr1[0]) and ver_dis(j,arr1[1]) and ver_dis(k,arr1[2])) or (ver_dis(i,arr2[0]) and ver_dis(j,arr2[1]) and ver_dis(k,arr2[2])):
                cnt +=1

print(cnt)

