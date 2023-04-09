# T = int(input())
#
# money = [25, 10, 5, 1]
# count = [0] * 4
#
# for i in range(T):
#     C = int(input())
#
#     for j in range(len(money)):
#         count[j] = C // money[j]
#         C = C % money[j]
#
#         print(' '.join(map(str, count)))

for _ in range(int(input())):
    C = int(input())
    NUM = [25, 10, 5, 1]
    li = []
    for n in NUM:
        li.append(C // n)
        C = C % n
    print(*li)
