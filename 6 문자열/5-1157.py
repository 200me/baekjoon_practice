abc = input().lower()
abc_list = list(set(abc))  # 중복 제거
num = []

for i in abc_list:
    count = abc.count(i)  # 개수 세는 함수
    num.append(count)

if num.count(max(num)) >= 2:
    print("?")
else:
    print(abc_list[(num.index(max(num)))].upper())
