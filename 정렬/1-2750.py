x = int(input())
num = []
for i in range(x):
    num.append(int(input()))
num_list1 = sorted(num)
for i in range(len(num)):
    print(num_list1[i])
