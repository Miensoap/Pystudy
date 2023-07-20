n,k=map(int,input().split())
arr=list(map(int,input().split()))

def is_possible(max_val):
    global k
    available_indices = [0,n-1] #경로
    for i in range(1,len(arr)-1):
        if arr[i] <= max_val: #작으면 밟아
            available_indices.append(i)
    available_indices.sort()
    arr_size = len(available_indices)
    for i in range(1, arr_size): #경로상의 점에 점프가능한지
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False

    return True


minmax = sum(arr)
for a in range(max(arr[0], arr[-1]), max(arr)+1): 
    if is_possible(a):
        minmax = min(minmax, a)

print(minmax)

