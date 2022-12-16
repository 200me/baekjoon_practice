total = int(input())
count = int(input())
plus = 0
for i in range(count):
    num1, num2 = map(int, input().split())
    plus += num1 * num2

if total == plus:
    print("Yes")
else:
    print("No")
