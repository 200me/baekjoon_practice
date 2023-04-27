N,M = map(int, input().split())
list_1 = list(map(int,input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for x in range(j+1, N):
            if list_1[i] + list_1[j] + list_1[x] > M:
                continue
            else:
                result = max(result, list_1[i]+ list_1[j]+ list_1[x])

print(result)
