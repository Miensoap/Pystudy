import sys
while True:
    arr=list(sys.stdin.readline().split())
    a,b=map(int,(arr[0],arr[1]))
    c=arr[2]
    print(a*b)
    if c=='C':
        break