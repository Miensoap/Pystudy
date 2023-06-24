c=int(input())
arr=list(map(int,input().split()))
jarr=[]
harr=[]
for elem in arr:
    if elem%2==0:
        jarr.append(elem)
    else:
        harr.append(elem)

a=len(jarr)
b=len(harr)

def jh(a,b):
    if b==1:
        return 2*b+1
    if a==b:
        return 2*b
    if a>b:
        return 2*b+1
    else:
        return(jh(a+1,b-2))

print(jh(a,b))

# 홀수가 10개 -> 짝수 ->10개 같으면 2홀수
# 짝수가 더 많아 -> 그냥 홀수개수*2+1=ans
# 홀수가 더 많아 -> 2개씩줄여 홀수 개수를 그리고 짝수를 1씩늘려 같아지거나 짝수가 더 많아질때까지해 =>