N = int(input())
M = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            M[i][j] = 1

answer = 0
for row in M:
    answer += row.count(1)
print(answer)
