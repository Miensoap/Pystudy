class dayinfo:
    def __init__(self,date,day,weather):
        self.day=day
        self.date=date
        self.weather=weather
    def info(self):
        print(self.date,self.day,self.weather)

n=int(input())
dayinfos=[]
for _ in range(n):
    dayinfos.append(dayinfo(*input().split()))
rainyday=[]
for elem in dayinfos:
    if elem.weather == 'Rain':
        rainyday.append(elem)

raindate=[]
for elem in rainyday:
    raindate.append(elem.date)

raindate.sort()
# print(raindate)

for i in range(len(rainyday)):
    if rainyday[i].date==raindate[0]:
        rainyday[i].info()
        break