n,m=map(int,input().split())
arr=list(map(int,input().split()))
#가능한 한 뒤에 설치한다.
cnt=0
while 1 in arr:
    for i in range(n):
        if arr[i]==1:
            #i에서 m만큼 뒤로가서 설치 -> i
            for j in range(i,i+(2*m)+1):
                if j==n:
                    break
                arr[j]=2
            cnt+=1

print(cnt)
