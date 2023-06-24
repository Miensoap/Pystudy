n=int(input())
arr=list(map(int,input().split()))

def solution(arr):
    from math import gcd                            # 최대공약수를 구하는 gcd() import
    answer = arr[0]                                 

    for num in arr:                                
        answer = answer*num // gcd(answer, num)     
    return answer

print(solution(arr))