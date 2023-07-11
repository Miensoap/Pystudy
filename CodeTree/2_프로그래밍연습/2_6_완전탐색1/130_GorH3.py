n, k = map(int,input().split())
arr = [tuple(input().split())for _ in range(n)]
placed = [0] * 10000

for elem in arr:
    if elem[1]=='G':
        placed[int(elem[0])-1] = 1
    else : 
        placed[int(elem[0])-1] = 2

max_cnt = 0

for i in range(10000 - k-1):
    candy_num = 0
    for j in range(i, i + k+1):
        candy_num += placed[j]

    max_cnt = max(max_cnt, candy_num)

print(max_cnt)