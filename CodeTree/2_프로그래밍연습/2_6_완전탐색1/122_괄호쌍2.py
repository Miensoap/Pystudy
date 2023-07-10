arr=list(input())
sum=0
for i in range(len(arr)-3):
    if arr[i]=='(' and arr[i+1]=='(':
        for j in range(i+2,len(arr)-1):
            if arr[j]==')'and arr[j+1]==')':
                sum+=1

print(sum)