MAX_NUM = 10000

n, k = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]
def count_num(l, r):
    cnt = 0
    for elem in arr:
        if l <= elem and elem <= r:
            cnt += 1

    return cnt

ans = 0
for i in range(1, MAX_NUM + 1):
    ans = max(ans, count_num(i, i + k))

print(ans)