class bom :
    def __init__(self,code,color,time):
        self.code=code
        self.color=color
        self.time=int(time)
    #method
    def info(self):
        print('code :',self.code)
        print('color :',self.color)
        print('second :',self.time)
    
#expected 4 argument = self+3arg(*input().split())
bom1=bom(*input().split())
bom1.info()
