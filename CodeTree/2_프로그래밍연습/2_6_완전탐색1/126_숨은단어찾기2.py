import sys
input = sys.stdin.readline
direction = [[0, 1], [1, 0], [1, 1], [1, -1],[0,-1],[-1,0],[-1,1],[-1,-1]]

def ver_lee(i,j,arr):
    cnt=0
    if arr[i][j] =='L':  
        for dir in direction:
            for k in range(1, 3):
                if in_range(i + (dir[0] * k), j + (dir[1] * k)):
                    if arr1[i + (dir[0] * k)][j + (dir[1] * k)] != 'E':
                        break
                    if k == 2:
                        # print(i,j)
                        cnt+=1
    return cnt
                        
def in_range(x,y):
    global n,m
    return 0<=x and x<n and 0 <=y and y<m

n,m=map(int,input().split())
arr1 = [list(input().rstrip()) for _ in range(n)]
sum=0

for i in range(n):
    for j in range(m):
        sum+=ver_lee(i,j,arr1)
            
print(sum)

