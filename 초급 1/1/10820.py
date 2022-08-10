# 10820 문자열 분석 //배고파서 그런가 집중이 잘 안됨
while True:
    try:
        answer = [0]*4
        k = list(input())
        for i in k:
            if i.islower():
                answer[0] += 1
            elif i.isupper():
                answer[1] += 1
            elif i.isdigit():
                answer[2] += 1
            else:
                answer[3] += 1
        print(" ".join(map(str,answer)))
    except EOFError:
        break