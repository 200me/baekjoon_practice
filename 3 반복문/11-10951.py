while True:
    try:
        num1, num2 = map(int, list(input().split()))
    except:
        break

    print(num1 + num2)