arr=list(map(int,input().split()))
ans=0
for i in range(arr[0],arr[1]+1):
    if arr[2] == i or arr[3] == i :
        ans+=1

for i in range(arr[2],arr[3]+1):
    if arr[0] == i or arr[1] == i :
        ans+=1

if ans>0:
    print('intersecting')
else:
    print('nonintersecting')