import sys
n = int(input())
string = input()
ans = 0
for i in range(1,101): # 길이
 
    twice = False
    for j in range(n-i+1): #시작
        for k in range(j+1, n-i+1): #비교시작
            is_same = True  
            for l in range(i): #길이만큼비교
                if string[j+l] != string[k+l]:
                    is_same = False
            if is_same == True: #뒤에 똑같은게 있으면
                twice = True
    if twice == False:
        print(i)
        sys.exit()
