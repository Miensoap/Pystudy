a,b,c=input().split()
a,c=int(a),int(c)

def plus(a,c):
    return(a+c)
def minus(a,c):
    return(a-c)
def mul(a,c):
    return(a*c)
def div(a,c):
    return(a//c)

if b =='+':
    result=plus(a,c)
    print(a,b,c,'=',result)
elif b =='-':
    result=minus(a,c)
    print(a,b,c,'=',result)
elif b=='*':
    result=mul(a,c)
    print(a,b,c,'=',result)
elif b=='/':
    result=div(a,c)
    print(a,b,c,'=',result)
else:
    print('False')


