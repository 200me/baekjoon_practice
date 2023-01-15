num = int(input())
a = list(map(int, input().split()))

b = max(a)
c = []
for i in a:
    c.append(i/b*100)
avg = sum(c)/num

print(avg)
