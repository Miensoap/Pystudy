#인자2개인함수
def print_rect(n, m):
    for i in range(n):
        print('1'*m)
n,m=map(int,input().split())
print_rect(n,m)