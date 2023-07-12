def able(num):
    for elem in arr:
        b=list(str(elem[0]))
        c1=elem[1]
        c2=elem[2]
        cnt1,cnt2=0,0

        for i in range(3):
            if num[i]==int(b[i]):
                cnt1+=1
            elif num[i]!=int(b[i]) and int(b[i]) in num:
                cnt2+=1
        if not (cnt1==c1 and cnt2==c2):
            return False      
        
    return True

n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
cnt=0

for i in range(1,10):
    for j in range(1,10):
            if j!=i:
                for k in range(1,10):
                    if k!=j and k!=i:
                        if able([i,j,k]):
                            cnt+=1

print(cnt)