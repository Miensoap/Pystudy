def dat(n,m):

    if not n<=12 :
        return 'No'
    if n==2:
        if not m<=28 :
            return 'No'
    elif n==4 or n==6 or n==9 or n==11:
        if not m<=30 :
            return 'No'
    else :
        if not m<=31:
            return 'No'

    return 'Yes'

a,b=map(int,input().split())

print(dat(a,b))

    

    

