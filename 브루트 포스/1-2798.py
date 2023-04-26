N,M = map(int, input().split())
list_1 = list(map(int,input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for x in range(j+1, N):