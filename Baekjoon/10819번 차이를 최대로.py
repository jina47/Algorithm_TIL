from collections import deque as dq

# 입력
N = int(input())
A = list(map(int, input().split()))

# left, right 나누기
A.sort()
if N%2 == 0:
    left = A[:N//2]
    right = A[N//2:]
else:
    left = A[:N//2+1]
    right = A[N//2+1:]
# left는 내림차순 정렬
left.sort(reverse=True)

# lst에 A 정렬하기
lst = dq([left[-1]])
left.pop()
i = 0
while True:
    # lst 정렬이 끝나면 break
    if len(lst) == N:
        break
    # i가 짝수이면 right에서 큰 숫자를 빼서 lst 양 끝에 넣어주기
    if i%2 == 0:
        lst.appendleft(right.pop())
        if right:
            lst.append(right.pop())
    # i가 홀수이면 left에서 큰 숫자를 빼서 lst 양 끝에 넣어주기
    else:
        lst.appendleft(left.pop())
        if left:
            lst.append(left.pop())
    i += 1

# answer에 lst 원소들 양 옆 차이의 절댓값을 담아줌
answer = []
for j in range(N-1):
    answer.append(abs(lst[j]-lst[j+1]))
# 맨 처음 값과 맨 마지막 값의 차이의 절댓값도 넣어줌
answer.append(abs(lst[0]-lst[-1]))
# answer의 합에서 가장 작은 값을 빼고 출력
print(sum(answer)-min(answer))


