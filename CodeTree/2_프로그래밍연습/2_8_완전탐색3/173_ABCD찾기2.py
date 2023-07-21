import sys
n=40
arr=list(map(int,input().split()))

for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            for l in range(n-i-j-k+1):
                A,B,C,D=i,j,k,l
                tarr=[A, B, C, D, A + B, B + C, C + D,
                        D + A, A + C, B + D, A + B + C,
                        A + B + D, A + C + D, B + C + D,
                        A + B + C + D
                      ]
                if sorted(tarr)==sorted(arr):
                    ans=[i,j,k,l]
                    for elem in sorted(ans):
                        print(elem, end=' ')
                    sys.exit()
print(-1)