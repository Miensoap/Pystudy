class Student:
    def __init__(self, a, number):
        self.a = int(a)
        self.number = int(number)

n=int(input())
aa=input().split()

students=[]
for i in range(n):
    students.append((Student(aa[i],i+1)))

students.sort(key=lambda x: (x.a))
nums=[]
#i번이 어디있는지 찾아

for i in range(n):
    for j in range(n):
        if students[j].number==i+1:
            nums.append(j+1)
            break

for elem in nums:
    print(elem,end=' ')
