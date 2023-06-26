class user :
    def __init__(self,g1,g2,num):
        self.g1=int(g1)
        self.g2=int(g2)
        self.num=num
    def info(self):
        print(self.num)

n=int(input())
users=[]
for i in range(n):
    users.append(user(*input().split(),i+1))

users.sort(key=lambda x: abs(x.g1) + abs(x.g2))

for elem in users:
    elem.info()     