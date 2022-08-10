# 10809 알파벳 찾기
w=input()
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in w: print(w.count(i),end=" ")
    else: print(0,end=" ")