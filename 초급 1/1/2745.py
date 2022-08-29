# 2745 진법 변환

l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = 0

alphabet, n = input().split()

n = int(n)
alphabet = list(alphabet)


for i in range(len(alphabet)):
    alphabet[i] = l.find(alphabet[i])

for i in range(len(alphabet)):
    answer = answer*n + alphabet[i]

print(answer)