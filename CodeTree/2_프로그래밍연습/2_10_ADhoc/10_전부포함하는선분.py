n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
arr.sort()
x1=[]
x2=[]
for i in range(n):
    x1.append(arr[i][0])
    x2.append(arr[i][1])
# x2.sort()
a1,a2 =x1[0],x2[0]
b1,b2=x1[n-1],x2[n-1]

# # 더많이줄어드는걸 없애
# # 양쪽에서다줄어드는경우 끝이 n-2[1]가아닐수도잇음
# a1,a2 =arr[0][0],arr[0][1]
# b1,b2=arr[n-1][0],arr[n-1][1]

if a2<=b2 :
    ach=x1[1]-a1
    bch=b2-arr[n-2][1]
else:
    ach=(arr[1][0]-a1)+(a2-b2)
    bch=0

# if ach>=bch:
#     arr.remove(arr[0])
# else:
#     arr.remove(arr[n-1])

# print(arr)
# print(arr[n-2][1]-arr[0][0])

