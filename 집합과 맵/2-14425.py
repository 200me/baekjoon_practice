N, M = map(int, input().split())
set_1 = []
set_2 = []
for i in range(N + M):
    sentence = input()
    if i < N:
        set_1.append(sentence)
    else:
        set_2.append(sentence)

set_1 = set(set_1)

cnt = 0
for i in set_2:
    if i in set_1:
        cnt += 1

print(cnt)
