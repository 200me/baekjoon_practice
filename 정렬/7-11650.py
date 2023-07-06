N = int(input())
list1 = []
for i in range(N):
    a, b = map(int, input().split())
    list1.append((a, b))
list1.sort()
for i in range(N):
    print(list1[i][0], list1[i][1])
