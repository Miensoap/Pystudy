def leap_year(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    
    if y % 400 == 0:
        return True
    
    return False

def season(m):
    if 3 <= m and m <= 5 :
        return 'Spring'
    elif 6 <= m and m <= 8 :
        return 'Summer'
    elif 9 <= m and m <= 11 :
        return 'Fall'
    elif m == 1 or m == 2 or m == 12  :
        return 'Winter'

def date_judge() :
    if leap_year(y) : # 윤년인 경우
        if m == 2 :
            if 1 <= d and d <= 29 :
                return season(m)
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 :
            if 1 <= d and d <= 31 :
                return season(m)
            else :
                return -1
        # else : 
        elif m == 4 or m == 6 or m == 9 or m == 11 :
            if 1 <= d and d <= 30 :
                return season(m)
            else :
                return -1    
            
    else : # 윤년이 아닌 경우
        if m == 2 :
            if 1 <= d and d <= 28 :
                return season(m)
            else :
                return -1
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 :
            if 1 <= d and d <= 31 :
                return season(m)
            else :
                return -1
        # else : 
        elif m == 4 or m == 6 or m == 9 or m == 11 :
            if 1 <= d and d <= 30 :
                return season(m)
            else :
                return -1

y, m, d = map(int, input().split())
result = date_judge()
print(result)
