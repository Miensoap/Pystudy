import sys
numbers=list(map(int,input().split()))

def get_diff(i, j, k,l):
    sum1 = numbers[i] + numbers[j]
    sum2 = numbers[k] + numbers[l]
    sum3 = sum(numbers) - sum1 - sum2
    if sum1!=sum2!=sum3 and sum1!=sum3:
        return abs(max(sum1,sum2,sum3)-min(sum1,sum2,sum3))
    else : return sys.maxsize


min_diff = sys.maxsize
for i in range(0, 5):
    for j in range(0,5):
        if i!=j:
            for k in range(0,5):
                if k!=i and k!=j :
                    for l in range(0,5):
                        if l!=i and l!=j and l!=k:
                            min_diff = min(min_diff, get_diff(i, j,k,l))

if min_diff==sys.maxsize:
    print(-1)
else:
    print(min_diff)