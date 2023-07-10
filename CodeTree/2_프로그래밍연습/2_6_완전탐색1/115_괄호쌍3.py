import sys
# arr=list(sys.stdin.readline().rstrip())
arr=list(input())
sum=0
for i in range(len(arr)):
    if arr[i]=='(':
        for j in range(i+1,len(arr)):
            if arr[j]==')':
                sum+=1

print(sum)