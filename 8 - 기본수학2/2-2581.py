M = int(input())
N = int(input())

num_list = []

for i in range(M, N + 1):
    ex = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                ex += 1
                break
        if ex == 0:
            num_list.append(i)
if len(num_list) > 0:
    print(sum(num_list))
    print(min(num_list))

else :
    print(-1)
