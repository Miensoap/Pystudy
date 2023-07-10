import sys
input = sys.stdin.readline
direction = [[0, 1], [1, 0], [1, 1], [1, -1]]

# def move1(x,y,dir_num) :
#     nx,ny = x+dx[dir_num],y+dy[dir_num]
#     return nx,ny

def ver_win(i,j,arr):
    if arr[i][j] != 0:  
        for dir in direction:
            for k in range(1, 5):
                if in_range(i + (dir[0] * k), j + (dir[1] * k)):
                    if arr1[i][j] != arr1[i + (dir[0] * k)][j + (dir[1] * k)]:
                        break
                    if k == 4:
                        print(arr1[i][j])
                        print(i + (dir[0] * 2) + 1, j + (dir[1] * 2) + 1)
                        sys.exit()

def in_range(x,y):
    global n
    return 0<=x and x<n and 0 <=y and y<n

n=19
arr1 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        ver_win(i,j,arr1)
            
print(0)

