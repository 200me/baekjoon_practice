A, B = [], []

N, M = map(int,input().split())

for i in [A, B]:
   for j in range(N):
    i.append(list(map(int, input().split())))

for j in 