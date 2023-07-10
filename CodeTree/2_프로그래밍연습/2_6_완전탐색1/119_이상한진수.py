arr=list(input())
max1=0
for i in range(len(arr)):
    narr=arr[:]
    if narr[i]=='0':
        narr[i]='1'
    else :
        narr[i]='0'
    # print(narr)

    num=int(''.join(narr),2)
    # print(''.join(narr))

    max1=max(max1,num)

print(max1)

    
