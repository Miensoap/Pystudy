arr=list(map(int,input().split()))
arr.sort()
a=arr[0]
b=arr[1]
c=arr[2]
abcd=arr[len(arr)-1]
bcd=arr[len(arr)-2]
acd=arr[len(arr)-3]
abd=arr[len(arr)-4]

cd=bcd-b
d=abd-a-b
c=cd-d

print(a,b,c,d)