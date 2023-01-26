word = input()
word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in word_list:
    word = word.replace(i, '*') # 단어를 *로 바꿔서 하나로 셀 수 있게함

print(len(word))
