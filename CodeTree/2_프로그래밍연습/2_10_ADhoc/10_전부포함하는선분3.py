# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(map(int,input().split()))
# # arr.sort()
# print(arr)
n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
arr.sort()
# print(arr)
# 더많이줄어드는걸 없애
if arr[1][0]-arr[0][0]>=arr[n-1][1]-arr[n-2][1]:
    arr.remove(arr[0])
else:
    arr.remove(arr[n-1])

print(arr[n-2][1]-arr[0][0])