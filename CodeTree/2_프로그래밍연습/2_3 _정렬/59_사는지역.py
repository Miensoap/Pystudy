class user:
    def __init__(self,name,addr,region):
        self.name=name
        self.addr=addr
        self.region=region
    def info(self):
        print('name',self.name)
        print('addr',self.addr)
        print('city',self.region)
    
n=int(input())
users=[]
for _ in range(n):
    name,addr,region=input().split()
    users.append(user(name,addr,region))

arr=[user.name for user in users]
arr.sort(reverse=True)
for i in range(n):    
    if users[i].name==arr[0]:
        users[i].info()
        break
    