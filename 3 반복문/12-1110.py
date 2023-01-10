n = int(input())
num = n
count = 0

while True:
    first = num // 10
    second = num % 10
    plus = (first + second) % 10
    num = (second * 10) + plus
    count = count + 1

    if (num == n):
        break

print(count)
