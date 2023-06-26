class user :
    def __init__(self,id='codetree',level=10):
        self.id=id
        self.level=int(level)

user1=user(*input().split())
user2=user()
print('user',user2.id,'lv',user2.level)
print('user',user1.id,'lv',user1.level)