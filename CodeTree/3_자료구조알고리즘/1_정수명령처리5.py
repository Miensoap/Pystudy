n=int(input())
arr=[]
for _ in range(n):
    c=input()
    if c == 'pop_back':
        arr.pop()
    elif c == 'size' :
        print(len(arr))
    elif c.startswith('push_back') : 
        _,num=c.split()
        arr.append(int(num))
    elif c.startswith('get') :
        _,num=c.split()
        print(arr[int(num)-1])