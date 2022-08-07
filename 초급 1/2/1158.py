# 1158 요세푸스 문제
import sys 
n, k = map(int,sys.stdin.readline().split())

people = list(range(1,n+1)) # 1~n번까지의 사람들로 이루어진 리스트 생성
save = [] # 제거후 저장할 리스트

cnt = 0

for i in range(n):
    cnt += k-1
    if cnt >= len(people): # 만약 카운트가 사람의 수를 넘어버리게 된다면
        cnt %= len(people) # 넘은만큼 카운트로 더해준다
    save.append(str(people[cnt])) # 새로운 리스트에 저장
    del people[cnt] # 옮겨진 사람은 원래 리스트에서 삭제

print("<",", ".join(save),">",sep="") # <3, 1, 2 ...>