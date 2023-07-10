# def RL(a):
#     if a=='R':
#         return 1
#     elif a=='L':
#         return -1

n =int(input())
narr=[0 for _ in range(2001)]
arr = [tuple(input().split()) for _ in  range(n)]
now=1000
for i in range(n):
    d = int(arr[i][0])
    # rl = RL(arr[i][1])

    # for j in range(now,now+d*rl,rl):
    #     narr[j]+=1; #블럭을 쌓아
    #     now+=rl
    if arr[i][1] == 'R':
        for i in range(now, now + d):
            narr[i] += 1
        
        now += int(d)
    
    elif arr[i][1] == 'L':
        for i in range(now - 1, now - d - 1, -1):
            narr[i] += 1
        now -=int(d)

sum=0
for elem in narr:
    if elem>=2:
        sum+=1

print(sum)
    