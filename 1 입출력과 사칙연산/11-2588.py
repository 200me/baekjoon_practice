first_num = int(input())
second_num = input()

num3 = int(second_num[0])
num2 = int(second_num[1])
num1 = int(second_num[2])

sum = 0

sum += first_num * num1
print(first_num * num1)

sum += 10 * first_num * num2
print(first_num * num2)

sum += 100 * first_num * num3
print(first_num * num3)

print(sum)