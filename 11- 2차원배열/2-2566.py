list1 = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= list1[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = list1[row][col]

print(max_num)
print(max_row, max_col)

# max_num = 0
#
# for i in range(9):
#     row = list(map(int, input().split()))
#     if max(row) > max_num:
#         max_num = max(row)
#         x = i + 1
#         y = row.index(max_num) + 1
# print(max_num)
# print(x,y)