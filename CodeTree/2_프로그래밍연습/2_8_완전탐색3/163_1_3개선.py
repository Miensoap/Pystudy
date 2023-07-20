import sys
n = int(input())
point = [tuple(map(int, input().split()))for i in range(n)]

def check_point3(i, j, k, check1, check2, check3):
    success = True

    for x, y in point:
        c1 = x
        c2 = x
        c3 = x

        if check1 == "y": c1 = y
        if check2 == "y": c2 = y
        if check3 == "y": c3 = y
        
        if c1 == i or c2 == j or c3 == k:
            continue

        success = False

    if success:
        return True
    else:
        return False

max_xy = 10
is_find = False

for i in range(max_xy + 1):
    for j in range(max_xy + 1):
        for k in range(max_xy + 1):
            # 이미 찾았으면 종료
            if is_find:
                print(1)
                sys.exit()

            # 모든 직선에 대해 시도
            if check_point3(i, j, k, 'x', 'x', 'x'): is_find = True  # 평행한 x축 3개 + 평행한 y축 0개
            if check_point3(i, j, k, 'x', 'x', 'y'): is_find = True  # 평행한 x축 2개 + 평행한 y축 1개
            if check_point3(i, j, k, 'x', 'y', 'y'): is_find = True  # 평행한 x축 1개 + 평행한 y축 2개
            if check_point3(i, j, k, 'y', 'y', 'y'): is_find = True  # 평행한 x축 0개 + 평행한 y축 3개

print(0)
