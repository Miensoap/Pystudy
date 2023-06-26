class goods :
    def __init__(self,name='codetree',code=50):
        self.name=name
        self.code=int(code)

    def info(self):
        print('product',self.code,'is',self.name)

good1=goods()
good2=goods(*input().split())
good1.info()
good2.info()

    
