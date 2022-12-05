one, two, three = map(int, list(input().split()))
price = 0
if one == two == three:
    price = 10000 + (one * 1000)

elif one == two:
    price = 1000 + one * 100
elif one == three:
    price = 1000 + one * 100
elif two == three:
    price = 1000 + two * 100
else:
    if one > two:
        one = one
    if one < two:
        one = two
    if one < three:
        one = three
    price = one * 100
print(price)
