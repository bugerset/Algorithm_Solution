# 17103 골드바흐 파티션
import sys

array = [True for i in range(1,1000001)]

for i in range(2,int(1000000**0.5)+1):
    if array[i] == True:
        j = 2
        while i * j < 1000000:
            array[i*j] = False
            j += 1

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    cnt = 0
    for j in range(2,num,1):
        if (j + num-j == num) and array[j] and array[num-j] and num-j != 1:
            cnt += 1
            if j > num -j:
                cnt -= 1
    print(cnt)