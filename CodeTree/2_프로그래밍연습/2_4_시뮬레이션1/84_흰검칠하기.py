n =int(input())
narr=[['n',0,0] for _ in range(200001)]
arr = [tuple(input().split()) for _ in  range(n)]
now=100001
cntW,cntB=0,0
for i in range(n):
    d = int(arr[i][0])

    if arr[i][1] == 'R':
        for i in range(now, now + d):
            if narr[i][0] !='G':
                narr[i][0] = 'B'
                narr[i][1]+=1
            if narr[i][1]>=2 and narr[i][2]>=2:
                narr[i][0]='G'
        now += d-1
    
    elif arr[i][1] == 'L':
        for i in range(now, now - d, -1):
            if narr[i][0] !='G':
                narr[i][0] ='W'
                narr[i][2]+=1
            if narr[i][1]>=2 and narr[i][2]>=2:
                narr[i][0]='G'
        now -= d-1

sumW,sumB,sumG=0,0,0
for i in range(len(narr)):
    if narr[i][0]=='W':
        sumW+=1
    elif narr[i][0]=='B':
        sumB+=1
    elif narr[i][0]=='G':
        sumG+=1

print(sumW,sumB,sumG)
    