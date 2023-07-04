n =int(input())
narr=[['n',0,0] for _ in range(200001)]
arr = [tuple(input().split()) for _ in  range(n)]
now=100001
cntW,cntB=0,0
for i in range(n):
    d = int(arr[i][0])

    if arr[i][1] == 'R':
        for i in range(now, now + d):
            narr[i][0] = 'B'
            narr[i][1]+=1
        now += d-1
    
    elif arr[i][1] == 'L':
        for i in range(now, now - d, -1):   
            narr[i][0] ='W'
            narr[i][2]+=1
        now -= d-1

sumW,sumB=0,0
for i in range(len(narr)):
    if narr[i][0]=='W':
        sumW+=1
    elif narr[i][0]=='B':
        sumB+=1

print(sumW,sumB)
    