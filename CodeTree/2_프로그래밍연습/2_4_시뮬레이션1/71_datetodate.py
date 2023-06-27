month1, day1, month2, day2 = map(int,input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dc=-day1 + 1 + day2

mdc=0
while month1 <month2:
    mdc+=num_of_days[month1]
    month1+=1

print(mdc+dc)

