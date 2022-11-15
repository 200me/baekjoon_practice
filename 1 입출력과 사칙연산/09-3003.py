import operator

list_1 = [1, 1, 2, 2, 2, 8]
list_2 = map(int, list(input().split()))
list_3 = list(map(operator.sub, list_1, list_2))
print(*list_3)
