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

dic = []

for o in other:
    dic[o] = 0

for c in card:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end=' ')
