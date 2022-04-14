# 입력 S, T
S = [s for s in input()]
T = [t for t in input()]

# S와 T의 길이가 같아질 때까지 T.pop()
while len(S) < len(T):
    # 만약 T의 맨 뒤 글자가 'B'이면 T를 뒤집어줌
    if T.pop() == 'B':
        T = list(reversed(T))

# S와 T가 같으면 1 출력, 아니면 0 출력
if S == T:
    print(1)
else:
    print(0)
    