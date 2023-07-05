n,m =map(int,input().split())
nmove=[tuple(input().split()) for _ in  range(n)]
mmove=[tuple(input().split()) for _ in  range(m)]

arrn = [100000]
arrm = [100000]

def move(arr,oarr):
    now=100000
    for i in range(len(arr)):
        d = int(arr[i][1])
        if arr[i][0] == 'R':
            for i in range(1, d+1):
                now += 1
                oarr.append(now)
        elif arr[i][0] =='L':
            for i in range(1,d+1):
                now -= 1
                oarr.append(now)
        

move(nmove,arrn)
move(mmove,arrm)

ans=0
for i in range(len(arrn)):
    if i!=0 and arrn[i]==arrm[i]:
        ans=i
        break

if ans == 0 :
    print(-1)
else:
    print(ans)


    