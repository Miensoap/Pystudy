a=input()
b=input()

def bubun(a,b):
    if b in a :
        return(a.index(b))
    else :
        return(-1)

print(bubun(a,b))

