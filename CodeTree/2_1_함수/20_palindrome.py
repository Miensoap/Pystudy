a=str(input())

def pali(a):
    # arr=list(a.split())
    # print(arr)
    for i in range(len(a)):
        if not a[i]==a[len(a)-1-i]:
            return 'No'
    return 'Yes'

print(pali(a))

