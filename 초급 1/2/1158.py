# 1158 요세푸스 문제
import sys 
n, k = map(int,sys.stdin.readline().split())

people = list(range(1,n+1)) # 1~n번까지의 사람들로 이루어진 리스트 생성
save = [] # 제거후 저장할 리스트

cnt = 0

for i in range(n):
    cnt += k-1
    if cnt >= len(people):
        cnt %= len(people)
    save.append(str(people[cnt]))
    del people[cnt]

print("<",", ".join(save),">",sep="")