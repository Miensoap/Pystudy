class user :
    def __init__(self,name,g1,g2,g3):
        self.name=name
        self.g1=int(g1)
        self.g2=int(g2)
        self.g3=int(g3)

    def info(self):
        print(self.name,self.g1,self.g2,self.g3)

n=int(input())
users=[]
for _ in range(n):
    users.append(user(*input().split()))

users.sort(key=lambda x: x.g1 + x.g2 + x.g3)

for elem in users:
    elem.info()

