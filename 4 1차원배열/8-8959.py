num = int(input())

for i in range(num):
    new_list = list(input())
    score = 0
    sum = 0
    for ox in new_list:
        if ox == 'O':
            score = score + 1
            sum += score
        else:
            score = 0
    print(sum)