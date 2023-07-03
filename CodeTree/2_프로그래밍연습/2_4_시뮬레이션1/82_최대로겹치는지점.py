k =int(input())
narr=[0 for _ in range(200)]
arr = [tuple(map(int,input().split())) for _ in  range(k)]
for i in range(k):
    s = arr[i][0]-1
    e = arr[i][1]

    for j in range(s,e):
        narr[j]+=1; #블럭을 쌓아

print(max(narr))
    