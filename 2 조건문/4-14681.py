# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y < 0:
#     print("4")

x = int(input())
y = int(input())
q = 0
sign = 1
if y < 0:
    q = 5
    sign = -1

if x < 0:
    q += 2 * sign
elif x > 0:
    q += sign
print(q)