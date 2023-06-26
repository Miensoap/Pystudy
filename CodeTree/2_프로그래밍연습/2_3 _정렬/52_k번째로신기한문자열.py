n,m,t=input().split()
n,m=int(n),int(m)
t=list(t)
words=[list(input()) for i in range(n)]
rem=[]
# for elem in sorted(words):
    # print(elem)
for j in range(n):
    for i in range(len(t)):
        if not t[i]==words[j][i]:
            # words.remove(words[j])
            rem.append(words[j])
            break
for i in range(len(rem)):
    words.remove(rem[i])
words.sort()
for elem in words[m-1]:
    print(elem,end='')
