N, L = map(int, input().split())

answer = []

# L=2 : n, n+1 = 2n+1
# L=3 : n-1, n, n+1 = 3n
# L=4 : n-1, n, n+1, n+2 = 4n+2
# L=5 : n-2, n-1, n, n+1, n+2 = 5n

for i in range(L, 101):
    # i가 짝수일 때, (N-i//2)가 i로 나누어지면 길이 i의 연속된 수의 합으로 N을 만들 수 있음
    if i % 2 == 0 and (N-i//2) % i == 0:
        N -= i//2
        for num in range(N//i-(i//2-1), N//i+(i//2+1)):
            answer.append(num)
        break
    # i가 홀수일 때, N이 i로 나누어지면 길이 i의 연속된 수의 합으로 N을 만들 수 있음
    elif i % 2 == 1 and N % i == 0:
        for num in range(N//i-i//2, N//i+i//2+1):
            answer.append(num)
        break

# 만약 answer에 아무 숫자도 없거나 answer[0]이 음수거나 answer 길이가 100이 넘는다면 -1 출력
if answer == [] or answer[0] < 0 or len(answer) > 100:
    print(-1)
else:
    print(' '.join(map(str, answer)))