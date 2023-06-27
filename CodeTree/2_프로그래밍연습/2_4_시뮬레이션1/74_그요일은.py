month1, day1, month2, day2 = map(int,input().split())
day=input()

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mdc=0
if month1==month2:
    dc =day2-day1
elif month1<month2:
    dc=(num_of_days[month1]-day1)+ day2
    while month1+1 <month2:
        mdc+=num_of_days[month1+1]
        month1+=1
# else:
#     dc=-((num_of_days[month2]-day2)+day1)
#     while month2+1 <month1:
#         mdc-=num_of_days[month2+1]
#         month2+=1
ch=dc+mdc

# if (ch)%7==0:
#     print('Mon')
# elif (ch)%7==1: 
#     print('Tue')
# elif (ch)%7==2:
#     print('Wed')
# elif (ch)%7==3:
#     print('Thu')
# elif (ch)%7==4:
#     print('Fri')
# elif (ch)%7==5:
#     print('Sat')
# elif (ch)%7==6:       
#     print('Sun')  
daycnt=[0 for _ in range(6)]
for i in range(ch%7):
    daycnt[i]+=1

if day=='Mon':
    print(ch//7)
elif day=='Tue' :
    print((ch//7)+daycnt[0])
elif day=='Wed' :
    print((ch//7)+daycnt[1])
elif day=='Thu' :
    print((ch//7)+daycnt[2])
elif day=='Fri' :
    print((ch//7)+daycnt[3])
elif day=='Sat' :
    print((ch//7)+daycnt[4])
elif day=='Sun' :
    print((ch//7)+daycnt[5])
    
   
