class sc:
    def __init__(self,code,loc,time) :
        self.code=code
        self.loc=loc
        self.time=int(time)
# a,b,c=input().split()
# sc1=sc(a,b,c)
# sc1=sc(lambda x: x,input().split())
# sc1 = sc(lambda a,b,c: (a,b,c) ,list(input().split()))
sc1=sc(*input().split())
print('secret code :',sc1.code)
print('meeting point :',sc1.loc)
print('time :',sc1.time)