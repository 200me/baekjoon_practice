A, B, C, D, E, F = map(int(input().split()))

result = []
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (A * i) + (B * j) == C and (D * i) + (E * j) == F:
            print(i, j)
            break
#런타임 에러

for i in range(2):
    print(result[i], end='')