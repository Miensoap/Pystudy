x,y=map(int,input().split())

cnt=0
for i in range(x,y+1):
    num=str(i)
    if len(str(i))%2==0:
        nums=num[:(len(num)//2)]
        nume="".join(reversed(num[(len(num)//2):]))
    else:
        nums=num[:(len(num)//2)]
        nume="".join(reversed(num[(len(num)//2+1):]))
     
    if  nums==nume :
        cnt+=1

print(cnt)