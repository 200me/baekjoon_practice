N = int(input())
A = [4]
F = 2
b = 1
sum = 0
for i in range(1, 16):
    F += b
    sum = F ** 2
    A.append(sum)
    b = b * 2
print(A[N])
