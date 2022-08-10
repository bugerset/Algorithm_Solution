# 17413 단어 뒤집기 2 //답지 참고함

import sys
word = list(sys.stdin.readline().rstrip())
i = 0
start = 0

while i < len(word): # 만약 i가 word의 글자수랑 같아진다면 루프 탈출

    if word[i] == "<": # <를 만나면
        i += 1 # i에 1을 추가
        while word[i] != ">": # 닫힌 괄호를 만날 때 까지
            i += 1  # i에 1을 추가
        i += 1 # 닫힌 괄호를 만난 후 i를 하나 증가시킨다

    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i # 시작하는 인덱스를 그동안 쌓아둔 i로 설정
        while i < len(word) and word[i].isalnum(): # i가 그 단어의 끝이아니고 숫자가 아니라면
            i+=1 # 계속 i에 1을 추가
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse() # 뒤집는다
        word[start:i] = tmp # word는 괄호에 있는 문자 빼고 뒤집은거로 저장해둠

    else: # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1 # 그냥 증가시킨다

print("".join(word)) # 단어 한줄로 출력

# <open>tag<close> 을 예시로 들어가겠다
# <를 만났으니 i += 1 / o p e n >
# >를 만날때까지 i는 5였고 마지막으로 i += 1을 해준다.
# 그 다음에 괄호가 끝난후 t라는 알파벳을 마주했으니까
# start = 6
# while문을 돌리면 i는 9가 된다
# tmp는 word[6:9]이고 이는 tag를 지칭한다
# 이 tag는 뒤집어준다.
# 이런식으로 해서 단어 뒤집기 2 완성