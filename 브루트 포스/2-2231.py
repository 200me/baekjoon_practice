N = int(input())

for i in range(1, N+1):
    num = sum(map(int,str(i)))
    inx = i+num

    if inx == N:
        print(i)
        break
    if i == N:
        print(0)