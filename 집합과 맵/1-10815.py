# N = int(input())
# card = list(map(int, input().split()))
# M = int(input())
# other = list(map(int, input().split()))
#
#
# for o in other:
#     if o in card:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

N = int(input())
card = list(map(int, input().split()))
M = int(input())
other = list(map(int, input().split()))

ord = []

for i in other:
    ord[i] = 0

for x in card:
    if x in ord:
        ord[x] = 1

for y in ord:
    print(ord[y], end=' ')
