import sys
binary=list(sys.stdin.readline().rstrip())
num = 0

for i in range(len(binary)):
    num = num * 2 + int(binary[i])

num*=17
digits = []

while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
