n=int(input())
arr = [tuple(input().split())for _ in range(n)]
lent=101
placed = [0] * lent

for elem in arr:
    placed[int(elem[0])] =elem[1]

maxlen=0


for j in range(lent):
    if placed[j]!=0: #사람있으면 시작
        st=j
    else : 
        st=lent
    cntG,cntH=0,0
    for k in range(st,lent):
        if placed[k]=='G':
            cntG+=1
            if cntG==cntH and cntG!=0:  #똑같아지면 길이
                len=k-st
                maxlen=max(maxlen,len)
        elif placed[k]=='H':
            cntH+=1
            if cntG==cntH and cntG!=0:  #똑같으면 길이
                len=k-st
                maxlen=max(maxlen,len)

    for k in range(st+1,lent):
        if placed[k]!=placed[k-1] : #st문자가안이어지면 길이
            len=k-st-1
            maxlen=max(maxlen,len)
            break
            
print(maxlen)