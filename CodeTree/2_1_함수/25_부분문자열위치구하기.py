a=input()
b=input()
def bubun(n,m):
    c=True
    #검사시작위치찾기
    for i in range(len(n)-(len(m)+1)):
        if m[0]==n[i]:
            #다 통과하면 return i / 틀리면 break
            for j in range(len(m)):
                if not m[j]==n[i+j]:
                    c=False
                    break
            if c:  
                return i  
    #같은게없어        
    return -1
        
    
print(bubun(a,b))
        