num1, num2 = map(int, input().split())
a = list(map(int, input().split()))
b = list()
for i in a:
    if i < num2:
        b.append(i)
print(*b)
