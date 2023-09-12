from string import ascii_uppercase

n,m,p = map(int,input().split())
mess = [tuple(input().split()) for _ in range(m)]
unread = int(mess[p-1][1])

names = list(ascii_uppercase)
users = []
for i in range(n):
    users.append(names[i])

# 문자 보냈으면 읽었음
for i in range(p-1,m): 
    if mess[i][0] in users:
        users.remove(mess[i][0])
    else :
        continue

for i in range(0,p-1):
    if int(mess[i][1]) == unread and mess[i][0] in users:
        users.remove(mess[i][0])
    
if unread >0:
    for elem in users:
        print(elem, end=" ")
