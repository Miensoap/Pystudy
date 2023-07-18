x,y=map(int,input().split())

cnt=0
for i in range(x,y+1):
    num=str(i)
    # temp=set()
    t1,t2=[],[]
    # for elem in num:
    #     temp.add(elem)
    temp=set(num)

    
    if len(temp)==2:
        for elem in num:
            if elem==num[0]:
                t1.append(elem)
            else:
                t2.append(elem)

        if min(len(t1),len(t2))==1:
            cnt+=1


print(cnt)


    
