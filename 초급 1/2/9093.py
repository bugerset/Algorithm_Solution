# 9093 단어 뒤집기
n = int(input())

for i in range(n):
    word = list(input().split())
    for j in range(len(word)):
        print((word[j])[::-1], end=" ")