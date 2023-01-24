num1, num2 = map(int, list(input().split()))

if int(str(num1)[::-1]) > int(str(num2)[::-1]) :
    print(int(str(num1)[::-1]))
elif int(str(num1)[::-1]) < int(str(num2)[::-1]) :
    print(int(str(num2)[::-1]))