word1 = []
length = []

for _ in range(5):
    word = input()
    word.append(word)
    length.append(len(word))

t = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            t += word1[j][i]





# c = [[0] * 15 for i in range(5)]
# for i in range(5):
#     d = list(input())
#     d_len = len(d)
#     for j in range(d_len):
#         c[i][j] = d[j]
# for i in range(15):
#     for j in range(5):
#         if c[j][i] == 0:
#             continue;
#         else:
#             print(c[j][i], end='')