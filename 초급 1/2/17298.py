# 17298 오큰수 // 시간초과로 답 인용
import sys

l = int(sys.stdin.readline()) # 횟수
num = list(map(int,sys.stdin.readline().split())) # 숫자 리스트 생성
stack = [] # 스택 생성
aw = [-1] * l # 답은 -1로 default 설정을 해준다.

for i in range(l):
    while stack and num[stack[-1]] < num[i]: # 스택에 숫자가 있고 
        # num[i]가 num의 x인덱스의 숫자보다 크면
        aw[stack.pop()] = num[i] # 답은 스택에서 제거한 인덱스에 num[i]를 저장
    stack.append(i) # 스택에 인덱스 0부터 1씩 추가

print(*aw) # 출력