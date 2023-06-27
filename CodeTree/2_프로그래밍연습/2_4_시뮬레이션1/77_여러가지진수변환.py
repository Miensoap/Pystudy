n,b=map(int,input().split())
digits = []

while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
