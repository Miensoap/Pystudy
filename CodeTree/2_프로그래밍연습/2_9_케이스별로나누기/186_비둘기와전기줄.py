n=int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
# arr.sort(key=lambda x: x[0])
bidul=[[] for _ in range(10)]

for elem in arr:
    bidul[elem[0]-1].append(elem[1])

cnt=0
for elem in bidul:
    for i in range(len(elem)):
        if i!=0 and elem[i] !=elem[i-1]:
            cnt+=1

print(cnt)
