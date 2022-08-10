# 11655 ROT13
word = list(input())
answer = ""
for i in word:
    if 65 <= ord(i) <= 90:
        if ord(i)+13 > 90:
            answer += chr(ord(i)-13)
        else:
            answer += chr(ord(i)+13)
    elif 97 <= ord(i) <= 122:
        if ord(i)+13 > 122:
            answer += chr(ord(i)-13)
        else:
            answer += chr(ord(i)+13)
    else:
        answer += i
print(answer)

# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))