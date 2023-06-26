class agent:
    def __init__(self,codename,score):
        self.codename=codename
        self.score=score

# #*input().split() = 2 argument
# #list expected at most 1 argument 
agents=[input().split() for _ in range(5)]

a=['A',101]
for i in range(len(agents)):
    if int(a[1])>int(agents[i][1]):
        a=agents[i]
for elem in a:
    print(elem,end=' ')

#TypeError: agent.__init__() missing 1 required positional argument: 'score'
#input().split() = 1 argument : class : list
# agent1=agent(input().split())

# TypeError: agent.__init__() takes 3 positional arguments but 4 were given
# (3개 입력했을 때) -> 4agument, expected 3
# agent1=agent(*input().split())

# print(type(agent1))
# print(agent1.codename)


