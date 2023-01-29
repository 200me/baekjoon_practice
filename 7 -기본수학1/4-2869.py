A, B, V = map(int, list(input().split()))
day = (V-B)/(A-B)

if day == int(day):
    print(int(day))

else:
    print(int(day+1))


