month1, day1, month2, day2 = map(int,input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mdc=0
if month1==month2:
    dc =day2-day1
elif month1<month2:
    dc=(num_of_days[month1]-day1)+ day2
    while month1+1 <month2:
        mdc+=num_of_days[month1+1]
        month1+=1
else:
    dc=-((num_of_days[month2]-day2)+day1)
    while month2+1 <month1:
        mdc-=num_of_days[month2+1]
        month2+=1



ch=dc+mdc

# print(ch)
if ch>0:
    if (ch)%7==0:
        print('Mon')
    elif (ch)%7==1: 
        print('Tue')
    elif (ch)%7==2:
        print('Wed')
    elif (ch)%7==3:
        print('Thu')
    elif (ch)%7==4:
        print('Fri')
    elif (ch)%7==5:
        print('Sat')
    elif (ch)%7==6:       
        print('Sun')   
else:
    if abs(ch)%7==0:
        print('Mon')
    elif abs(ch)%7==1: 
        print('Sun')
    elif abs(ch)%7==2:
        print('Sat')
    elif abs(ch)%7==3:
        print('Fri')
    elif abs(ch)%7==4:
        print('Thu')
    elif abs(ch)%7==5:
        print('Wed')
    elif abs(ch)%7==6:       
        print('Tue')   
