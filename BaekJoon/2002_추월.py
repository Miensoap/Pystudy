# n=int(input())
# arr1=[input() for _ in range(n)] 
# arr2=[input() for _ in range(n)]
# cnt=0
# for i in range(len(arr1)):
#     # #순서가 앞으로오면
#     # if arr2.index(arr1[i])< i:
#     #     cnt+=1
#     #원래 내앞에잇던애가 뒤에있으면
#     a=False
#     for j in range(0,i):
#         if arr2.index(arr1[j])>arr2.index(arr1[i]):
#             a=True
#     if a:
#         cnt+=1
# print(cnt)

import sys

L1,L2=[],[]
N=int(sys.stdin.readline())

for i in range(N):
    L1.append(sys.stdin.readline())
for i in range(N):
    L2.append(sys.stdin.readline())

ans=0

for l in L2:
    if L1.index(l) != 0:
        ans+=1
        L1.remove(l)
    else: L1.remove(l)        

print(ans)
