n = int(input())

class su:
    def init(self, num, _num):
        self.num, self._num = num, _num

m = list(map(int, input().split()))

judge = []
for i in range(n):
    judge.append(su((m[i]), i+1))

judge.sort(key = lambda x : x.num)

print()
for su in judge:
    print(su._num, end = ' ')