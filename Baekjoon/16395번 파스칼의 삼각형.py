n, k = map(int, input().split())

# 숫자를 담아줄 리스트
pascal = [[0 for _ in range(n)] for _ in range(n)]
pascal[0][0] = 1

# 이항계수 계산
for r in range(1, n):
    for i in range(r+1):
        # 첫 항이나 마지막 항은 무조건 1
        if i == 0 or i == r:
            pascal[r][i] = 1
        # 그 외 항은 전 행의 이전 열과 현재 열의 값의 합
        else:
            pascal[r][i] = pascal[r-1][i-1] + pascal[r-1][i]

# 출력
print(pascal[n-1][k-1])