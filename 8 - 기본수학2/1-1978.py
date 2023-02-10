N = int(input())
num = map(int, list(input().split()))
count = 0

for i in num:
    error = 0
    if (i == 1):
        continue
    for j in range(2, i + 1):
        if (i % j == 0):
            error += 1

    if (error == 1):
        count += 1
print(count)
