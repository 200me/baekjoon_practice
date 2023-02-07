N = int(input())
dr = 0

while N >= 0 :
    if N % 5 == 0:
        dr += N // 5
        print(dr)
        break
    N -= 3
    dr += 1
else :
    print(-1)

