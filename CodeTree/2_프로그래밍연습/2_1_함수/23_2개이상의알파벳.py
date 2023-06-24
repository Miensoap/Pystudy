a=str(input())

def pali(a):
    # arr=list(a.split())
    # print(arr)
    for i in range(len(a)):
        tem=a[i]
        for i in range(len(a)):
            if tem!=a[i]:
                return 'Yes'
    return 'No'

print(pali(a))