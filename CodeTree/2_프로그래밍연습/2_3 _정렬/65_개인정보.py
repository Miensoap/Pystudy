class user :
    def __init__(self,name,hei,wei):
        self.name=name
        self.hei=int(hei)
        self.wei=float(wei)

    def info(self):
        print(self.name,self.hei,round(self.wei,1))

users=[]
for _ in range(5):
    users.append(user(*input().split()))

users.sort(key=lambda x: x.name)
print('name')
for elem in users:
    elem.info()
users.sort(key=lambda x:-x.hei)
print('\nheight')
for elem in users:
    elem.info()