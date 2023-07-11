import sys
numbers=list(map(int,input().split()))

def get_diff(i, j, k):
    sum1 = numbers[i] + numbers[j] + numbers[k]
    sum2 = sum(numbers) - sum1
    return abs(sum1 - sum2)


min_diff = sys.maxsize
for i in range(0, 4):
    for j in range(i + 1, 5):
        for k in range(j+1,6):
            min_diff = min(min_diff, get_diff(i, j,k))

print(min_diff)