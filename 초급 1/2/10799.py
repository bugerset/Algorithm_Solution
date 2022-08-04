# 10799 쇠막대기
c=input()
a=0
e=0
for i in range(len(c)):
    if c[i] == "(":
        e += 1
    else:
        if c[i-1] == "(":
            e -= 1
            a += e
        else:
            a += 1
            e -= 1
print(a)