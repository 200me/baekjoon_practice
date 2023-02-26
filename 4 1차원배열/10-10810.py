N, M = map(int, input().split())
ba = [0] * (N + 1)

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, j + 1, 1):
        ba[y - 1] = k
for x in range(N):
    print(ba[x], '', end='')
