from collections import deque as dq

N, K = map(int, input().split())
circle = dq([n for n in range(1, N+1)])
answer = []

# answer에 숫자들이 다 채워질 때까지 반복
while len(answer) < N:
    # circle의 길이가 K보다 작을 때
    if len(circle) < K:
        # K를 circle의 길이로 나눴을 때 나머지만큼을 new_K로 설정
        new_K = K%len(circle)
        # new_K가 0이 아닐 때 제거해야 하는 수 이전의 수는 뒤에 붙여주고 제거해야 하는 수는 제거 (answer에 넣어줌)
        if new_K != 0:
            for _ in range(new_K-1):
                circle.append(circle.popleft())
            answer.append(circle.popleft())
        # new_K가 0이면 맨 끝의 수를 제거
        else:
            answer.append(circle.pop())
    # circle의 길이가 K보다 크거나 같을 때
    else:
        # 제거해야 하는 수 이전의 수는 뒤에 붙여주고 제거해야 하는 수는 제거
        for _ in range(K-1):
            circle.append(circle.popleft())
        answer.append(circle.popleft())

# 출력
for i, num in enumerate(answer):
    if i == 0:
        print('<', end='')
    if i != N-1:
        print(str(num)+', ', end='')
    elif i == N-1:
        print(str(num)+'>')

