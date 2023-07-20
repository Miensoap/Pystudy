import sys
n=int(input())
arr=[tuple(map(int,input().split()))for _ in range(n)]

for i in range(11):
    for j in range(11):
        for k in range(11):
            line=(i,j,k)
            suc=True
            
            for elem in arr: #30
                ok=0
                if not elem[0] in line:
                    break
                ok+=1
                if not(elem[0]==i or elem[0]==j) or not elem[1]==k:
                    break
                ok+=1
                if not(elem[1]==i or elem[1]==j) or not elem[0]==k:
                    break 
                ok+=1
                if not elem[1] in line:
                    break
                ok+=1
    
        
            if ok>0:
                print(1)
                sys.exit()

print(0)


            

            

            


