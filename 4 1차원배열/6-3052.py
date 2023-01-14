a = list()
count = 0
for i in range(10):
    num = int(input())
    num = num % 42
    if num not in a:
        a.append(num)
        count = count+1
    else:
        count = count

print(count)


