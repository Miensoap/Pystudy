arr=list(map(int,input().split()))
# a=min(arr)
# abc=max(arr)
# bc=abc-a
arr.sort()
a=arr[0]
b=arr[1]
abc=arr[6]
bc=arr[5]
c=bc-b
print(a,b,c)