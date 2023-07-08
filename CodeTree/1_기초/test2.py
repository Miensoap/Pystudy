# print((lambda a,b : a+b)(3,7))
# # print(lambda a,b : a+b, 3,7)
# print((lambda a : a) 3)

# # sorted(array, key=lambda x: x[1]) # x를받아서 x[1] 반환
# # result = map(lambda a,b : a+b , list1,list2)

# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# b = [i for i in a if i > 5 and i < 10]
# print(a,b,sep='\n')

# from functools import reduce
# c=reduce(lambda x,y : x+y,a)

# print(c)

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 
         'table.xslx', 'spec.docx']

print(list(filter(lambda x : x.find('jpg') != -1 or x.find('png') != -1, files)))
#lambda 함수에 x인자로 file의 요소를 받아서 x.find()를 호출. 없으면 -1 반환.
#lambda 반환값에 조건식사용 : True or False 반환.
#filter는 함수(lambda)의 반환값이 True면 요소를 반환. -> list에저장.