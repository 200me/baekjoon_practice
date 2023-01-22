abc = input().upper()
abc_list = list(set(abc))  # 중복 제거
num = []

for i in abc:
    count = abc.count  # 개수 세는 함수
    num.append(count(i))

if num.count(max(num)) > 1:
    print("?")
else:
    print(abc_list[(num.index(max(num)))])
