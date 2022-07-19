# 입력값 N
N = int(input())

# 매 자리 수마다 가능한 개수 세기
fibo = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N-1):
    new = [0 for _ in range(10)]
    for j in range(10):
        # 이전 숫자가 0이면 다음에 1만 가능, 이전 숫자가 9이면 다음에 8만 가능
        if j == 0:
            new[1] += fibo[j]
        elif j == 9:
            new[8] += fibo[j]
        # 이전 숫자가 1~8이면 다음에 가능한 수는 j-1, j+1
        else:
            new[j-1] += fibo[j]
            new[j+1] += fibo[j]
    fibo = new

# 계단 수의 총 개수는 sum(fibo)
print(sum(fibo)%1000000000)
