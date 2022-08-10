# 1406 에디터 (시간초과로 답 인용) ([],[]로 나눠서 L,D에 따라 구분한다)
import sys

word = list(sys.stdin.readline().rstrip()) # 좌 리스트
word2 = [] # 우 리스트

for i in range(int(sys.stdin.readline())):
    key = sys.stdin.readline().split()
    if key[0] == "L" and word : # 커서를 좌로 움직여야 하면
        word2.append(word.pop()) # 좌 리스트에 있는 마지막 알파벳을 우 리스트로 이동
    elif key[0] == "D" and word2 : # 우로 움직여야 하면
        word.append(word2.pop()) # 우 리스트에 있는 마지막 알파벳을 좌 리스트로 이동
    elif key[0] == 'B' and word : # 커서의 왼쪽 알파벳을 지운다면
        word.pop() # 그냥 좌 리스트에서 지우면 된다
    elif key[0] == "P": # 입력을 한다면
        word.append(key[1]) # 그냥 좌 리스트에 저장
        
word.extend(reversed(word2)) # 좌 리스트에 우 리스트를 붙히는데 append로 인해 
# 우 리스트는 거꾸로 저장이 되어있으므로 reversed를 통해 다시 설정한후 붙혀준다
print(''.join(word)) # for문 대신 사용

# extend|라는 단어를 에디터 해보자
# L이면 exten|d
# LL이면 ext|dne
# D면 exte|nd
# B면 왼쪽리스트인  exte|에서 e를 pop()
# P면 ext()| ()에 단어추가
# 최종적으로 붙힐때는 우측 리스트는 역순으로 저장되어 있으므로 리버스해서 Extend해준다