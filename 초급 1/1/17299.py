# 17299 오등큰수 // 카운팅 하는 방법만 찾아봄
# // from collections import Counter 이라는 것을 공부해두자
import sys
from collections import Counter

n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().split()))
answer = [-1] * n
stack = [] # 스택으로 한번에 처리
cnt = {} # 카운팅

for i in nl:
    try:
        cnt[i]+=1 # [숫자의 개수를 +1 하는거]
    except: # 구색맞추기
        cnt[i]=0

for i in range(n):
    while stack and cnt[nl[stack[-1]]] < cnt[nl[i]]: # 스택에 수가 있고 
        # 스택의 마지막 인덱스를 nl에 대입했을때 그 숫자의 갯수가 nl[i]숫자의 갯수보다 많으면
        answer[stack.pop()] = nl[i] # 스택의 마지막 인덱스를 빼버리고 그 숫자로 답을 채운다
    stack.append(i) # 스택에 i를 채워준다

print(*answer) # 출력