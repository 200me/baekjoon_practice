N, M = map(int, input().split())
data = [i for i in range(N + 1)]

<<<<<<< HEAD
for _ in range(M):
    i, j = map(int, input().split())
    value = []
    for k in range(i, j + 1):
        value.append(data[k])

    value = value[::-1]
    number = 0
    for k in range(i, j + 1):
        data[k] = value[number]
        number += 1

for k in range(1, len(data)):
    print(data[k], end=' ')
=======
for _ in range(m) :
  i, j = map(int, input().split())
  value = []
  for k in range(i, j + 1) :
>>>>>>> e6899936b4232275435a7010b35d57699bd267c3
