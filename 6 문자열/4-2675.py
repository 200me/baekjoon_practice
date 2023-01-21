T = int(input())

for i in range(T):
    num, word = input().split()
    for j in word:
        print(j*int(num), end='')
    print()

