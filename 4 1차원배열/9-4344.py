num = int(input())

for i in range(num):
    count = 0
    a = list(map(int, input().split()))
    b = a[1:]
    c = a[0]
    plus = sum(b) / c
    for i in range(c):
        if plus < b[i]:
            count = count + 1

        d = int(a[0])

        fra = count / d
        dec_num = fra * 100

    #print(round(dec_num, 3)) 소수점 끝자리가 0일때 3번째까지 안나옴

    print("{:.3f}%".format(dec_num)) #무조건 3번째까지 출력 가능
