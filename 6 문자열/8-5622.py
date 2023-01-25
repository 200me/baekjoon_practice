word = str(input())
wd = list(word)
word_len = len(word)

num = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0


for i in range(word_len):
    for j in range(len(num)):
        if word[i] in num[j]:
            time += num.index(num[j])+2

print(time)


