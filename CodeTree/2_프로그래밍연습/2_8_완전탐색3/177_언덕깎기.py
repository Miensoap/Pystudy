import sys

INT_MAX = sys.maxsize
MAX_N = 1000
MAX_H = 100

n = int(input())
k = 17
arr = [int(input()) for _ in range(n)]
ans = INT_MAX

for i in range(MAX_H):
    cost = 0
    for j in range(n):
        if arr[j] < i:
            cost += (arr[j] - i) * (arr[j] - i)
        if arr[j] > i + k:
            cost += (arr[j] - i - k) * (arr[j] - i - k)

    ans = min(ans, cost);

print(ans)