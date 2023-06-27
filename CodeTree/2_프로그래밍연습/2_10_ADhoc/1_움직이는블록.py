n=int(input())
arr=[int(input()) for _ in range(n)]

sum=0
for elem in arr:
    sum+=elem
avg=sum//n
cnt=0
for elem in arr:
    if elem>avg:
        cnt+=elem-avg

print(cnt)

