d2,t2,m2=map(int,input().split())
d1,t1,m1=11,11,11
#앞뒤 남는시간 = 12시간 / 13시간
tc1=24-(t1+1)
tc2=t2
#앞뒤 남는 분 = 49분 / 14분
mc1=60-m1 
mc2=m2
tmc=(60*(tc1+tc2)+mc1+mc2)
#날짜차이 0
dct=(-(d1+1) + d2)*24*60

if dct+tmc>=0:
    print(dct+tmc)
else :
    print(-1)
