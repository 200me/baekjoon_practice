N = int(input())
result =""
for i in range(1, int(N/4)+1):
    if i != (N/4):
        result += "long"

    else:
        result += "long int"

print(result)

