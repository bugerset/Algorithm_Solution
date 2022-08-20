# 1212 8진수 2진수

n = int(input())
a = []

while n!=0:
    if n%-2 == -1:
        a.append("1")
        n = (n//-2)+1
    else:
        a.append("0")
        n = n//-2


a.reverse()
if len(a) > 0:
    print("".join(a))
else:
    print(0)

# -13/-2  -2*7+1
# 7/-2    -2*-3+1
# -3/-2    -2*2+1
# 2/-2     -2*-1+0
# -1/-2    -2*1+1
# 1/2      -2*0+1