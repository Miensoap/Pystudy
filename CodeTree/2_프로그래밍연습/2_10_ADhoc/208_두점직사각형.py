x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())

hei=max(y1,y2,b1,b2)-min(y1,y2,b1,b2)
bro=max(x1,x2,a1,a2)-min(x1,x2,a1,a2)

print(hei*bro)
