# 9012 괄호
n = int(input())

for i in range(n):
    k = list(input())
    for j in range(len(k)):
        if "(" in k:
            if ")" in k:
                if k[0] == ")" or k[-1] == "(":
                    break
                else:
                    k.remove(")")
                    k.remove("(")
                    
            if len(k) < 1:
                print("YES")
    if len(k) >= 1:
        print("NO")