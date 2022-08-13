# 입력
N = int(input())
T, P = [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

# 최대 이익 maxprofit
maxprofit = 0

# 최대 이익 구하는 함수 counsel
def counsel(start, profit):
    global maxprofit

    # 만약 start + T[start]가 N+1을 넘는다면 return
    if start + T[start] > N+1:
        # 구한 profit이 maxprofit보다 크면 maxprofit 갱신
        if profit > maxprofit:
            maxprofit = profit
        return
    
    # 만약 start + T[start]가 N+1보다 작거나 같다면 상담 가능
    else:
        # profit에 P[start]를 더해주고 start에는 T[start]를 더해줌
        profit += P[start]
        start += T[start]
        # 새롭게 구한 start가 N+1과 같으면 더 이상 상담을 진행할 수 없으므로 return
        if start == N+1:
            if profit > maxprofit:
                maxprofit = profit
                return
        # start부터 N까지 다시 counsel 실행
        for i in range(start, N+1):
            counsel(i, profit)


# 모든 날짜에 대해 시작점으로 두고 counsel 실행 maxprofit 구하기
for i in range(1, N+1):
    counsel(i, 0)

# 출력
print(maxprofit)


    
