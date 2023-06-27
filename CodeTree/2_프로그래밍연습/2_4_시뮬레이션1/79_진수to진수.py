import sys
a,b=map(int,input().split())
n=list(sys.stdin.readline().rstrip())
#a진수n을 10진수로
num = 0
for i in range(len(n)):
    num = num * a + int(n[i])
n=num
#10진수n을 b진수로바꿔줘
digits = []
while True:
    if n < b:
        digits.append(n)
        break
    digits.append(n % b)
    n //= b

for digit in digits[::-1]:
    print(digit, end="")
