# 1874 스택수열
import sys
n = int(sys.stdin.readline()) # 반복할 횟수

answer = [] # +,-
nl = [] # 현재 리스트에 얼마나 있는가
cnt = 0
k = 0

for i in range(n):
    num = int(sys.stdin.readline()) # 스택수열에 넣을 숫자
    while cnt < num: # 카운트가 입력받은 num보다 작다면
        cnt += 1 # 카운트를 하나씩 올려주고
        answer.append("+") # 정답란에 +를 추가
        nl.append(cnt) # nl에 cnt를 집어넣어 반례 확인

    if nl[-1] == num: # 만약 그 nl리스트의 마지막이 입력받은 num과 같다면
        nl.pop() # nl리스트의 마지막을 제거한다
        answer.append('-') # 정답란에 -를 추가
    else:
        k = 1 # 반례설정
    
if k == 1: # 반례가 나오면
    print("NO") # 결론적으론 안되는거다
else:
    for i in answer:
        print(i)