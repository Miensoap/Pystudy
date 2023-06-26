class user:
    def __init__(self,name,hei,wei):
        self.name=name
        self.hei=hei
        self.wei=wei
    def info(self):
        print(self.name,self.hei,self.wei)
    
    
n=int(input())
users=[]
for _ in range(n):
    users.append(user(*input().split()))

users.sort(key=lambda x: x.hei)

for user in users:
    user.info()