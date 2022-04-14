import sys

# 단어의 개수 N
N = int(input())

# 단어들 모음 리스트
words = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in words:
        words.append(word)

words.sort(key=lambda x: (len(x),x))

for word in words:
    print(word)
