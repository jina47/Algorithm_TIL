# 입력
N = int(input())

# 1이면 0~9 10개
# 2이면 00~99 10+9+..+1 = 55개

# 시작하는 숫자를 각 인덱스라고 했을 떄 가능한 개수 담아주기(N=1인 경우)
start = [1 for _ in range(10)]

# 길이가 N인 오르막 수 개수 구하기
for i in range(1, N):
    # i 길이의 전체 오르막 수는 sum(start) 
    total = sum(start)
    # i+1 길이의 오르막 수를 담는 new_start 리스트
    # 0으로 시작하는 수의 개수는 total
    # 1로 시작하는 수의 개수는 total-start[0]
    # 9로 시작하는 수의 개수는 total-(start[0]+start[1]+...+start[8])
    new_start = [total]
    for j in range(0, 9):
        total -= start[j]
        # 최종 개수에 10007로 나눈 나머지를 구할 것이므로 연산 중간에도 효율성을 위해 나눠줌
        new_start.append(total%10007)
    # start를 new_start로 갱신
    start = new_start


# 출력
print(sum(start)%10007)



