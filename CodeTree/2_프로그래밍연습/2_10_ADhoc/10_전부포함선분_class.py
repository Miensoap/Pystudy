class sun:
    def __init__(self,x1,x2):
        self.x1=int(x1)
        self.x2=int(x2)
    def info(self):
        print(self.x1,self.x2)

n=int(input())
arr=[sun(*input().split())for _ in range(n)]

x1sort=sorted(arr,key=lambda x : x.x1) #x1순으로 정렬된 arr
x2sort=sorted(arr,key=lambda x : x.x2) #x2순으로 정렬된 arr
#x1sort[0] or x2sort[n-1] 지울거야

ach=x1sort[1].x1-x1sort[0].x1 #1지웠을때 줄어드는길이
bch=x2sort[n-1].x2-x2sort[n-2].x2 #2지웠을때 줄어드는길이

# print('ch',ach,bch)

if ach>bch:
    # print('x1')
    # x1sort[0].info()
    x1sort.remove(x1sort[0])
else:
    # print('x2')
    # x2sort[n-1].info()
    x2sort.remove(x2sort[n-1])

print(x2sort[len(x2sort)-1].x2-x1sort[0].x1)




