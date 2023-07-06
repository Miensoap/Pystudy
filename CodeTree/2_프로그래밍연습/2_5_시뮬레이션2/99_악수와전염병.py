n,k,p,T=map(int,input().split())
acsu = [list(map(int, input().split())) for _ in range(T)] 
acsu.sort(key=lambda x : x[0])
ac_cnt = [0 for _ in range(n)] # 악수한 횟수
apge = set() #전염시키는사람
apah = [0 for _ in range(n)] #전염된사람

apge.add(p)
apah[p-1]=1

for i in range(len(acsu)):
    t=acsu[i][0]
    x,y=acsu[i][1],acsu[i][2]

    for i in range(len(ac_cnt)): #악수 k번하면 지움
        if ac_cnt[i-1]>=k :
            if i in apge:
                apge.remove(i)
            ac_cnt[i-1]=0

   
    # if apah[x-1] == 1:
    #     if ac_cnt[x-1] < k:
    #         apah[y-1] = 1
    #         ac_cnt[x] += 1

    # elif apah[y-1] == 1:
    #     if ac_cnt[y-1] < k:
    #         apah[x-1] = 1
    #         ac_cnt[y] += 1 



    # if x in apge or y in apge:
    #     apge.add(x)
    #     apge.add(y)
    #     apah[x-1]=1
    #     apah[y-1]=1
    #     ac_cnt[x-1]+=1 #악수를해
    #     ac_cnt[y-1]+=1
        

for elem in apah:
    print(elem,end='')


