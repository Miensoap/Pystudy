class user:
    def __init__(self,name,kor,eng,mat):
        self.name=name
        self.kor=int(kor)
        self.eng=int(eng)
        self.mat=int(mat)
    def info(self):
        print(self.name,self.kor,self.eng,self.mat)

n=int(input())
users=[]
for _ in range(n):
    users.append(user(*input().split()))
users.sort(key=lambda x : (-x.kor, -x.eng, -x.mat))

for elem in users:
    elem.info()