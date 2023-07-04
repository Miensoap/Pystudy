n=int(input())
arr=list(map(int,input().split()))
arrs=sorted(arr)
cnt=0
while arr!=arrs :

    for i in (n-1,1,-1):
        a=101
        if abs(arr[0]-a)>abs(arr[0]-arr[i]):
            a=arr[i]
            break
    cnt+=1
    if arr[0]<a:
        arr.insert(arr.index(a),arr[0])
    else :
        arr.insert(arr.index(a)+1,arr[0])
    arr.pop(0)

print(cnt)
    
# n = int(input())  # 수열의 크기를 입력받습니다.
# a = list(map(int, input().split()))  # 수열을 입력받습니다.

# if n !=1:
#     cnt =0
#     for i in range(n-1,0,-1):
#         if a[i-1] > a[i]:
#             break
#         cnt +=1
#     print(n-cnt-1)
# else:
#     print(1)



