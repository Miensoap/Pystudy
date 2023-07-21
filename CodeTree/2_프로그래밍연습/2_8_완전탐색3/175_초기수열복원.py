n=int(input())
arr=list(map(int,input().split()))
answer=[]

for i in range(n):
    suc=True
    temp=[0 for _ in range(n)]
    temp[0]=i+1 #1번넣어봐
    exist=[False for _ in range(n+1)]
    for j in range(n-1):
        diff = arr[j]-temp[j] #차이
        if diff <=0 or diff>n: # 더작아지거나 n을넘어가면 실패
            suc=False
            break
        if exist[diff]: #이미썻어도 실패
            suc=False 
            break
        exist[diff]=True
        temp[j+1]=diff
    if suc:
        print(*temp)
        break
