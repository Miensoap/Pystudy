a=0
def hj(n):
    global a
    if n==1:
        return a
    a+=1
    if n%2==0:
        return(hj(n//2))
    else:
        return(hj(n*3+1))
    

print(hj(int(input())))

