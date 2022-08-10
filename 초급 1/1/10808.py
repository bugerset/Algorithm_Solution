# 10808 알파벳 개수
word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
dic = dict()

for i in alpha:
    dic[i] = 0
for i in word: 
    dic[i] += 1

for value in dic.values():
    print(value, end=" ")