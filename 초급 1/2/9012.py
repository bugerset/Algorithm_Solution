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

# 1. (((()())()
# "("이 있고 ")"도 있으니까 "()"제거 -> (((())()
# 반복 -> ((()() -> ((() -> ((
# k의 마지막이 -1이니까 스탑
# k리스트의 길이가 1 이상이니까 No

# 2. (()())((()))
# (())((())) -> ()((())) -> ((())) -> (()) -> () -> None
# Yes