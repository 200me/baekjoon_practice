N = int(input())
dr = 0
five = N // 5
three = N // 3
five1 = N % 5
three1 = N % 3

if five1 == 0:
    dr += five
    print(dr)
elif not five1 == 0:
    dr = N//5
