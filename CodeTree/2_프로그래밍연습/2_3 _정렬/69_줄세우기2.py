class Student:
    def __init__(self, hei, wei, number):
        self.hei = int(hei)
        self.wei = int(wei)
        self.number = int(number)
    def info(self):
        print(self.hei,self.wei,self.number)

n=int(input())
stuents=[]
for i in range(n):
    stuents.append((Student(*input().split(),i+1)))

stuents.sort(key=lambda x: (x.hei,-x.wei))
for elem in stuents:
    elem.info()