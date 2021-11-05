# 테스트 케이스 수 T
T = int(input())

for _ in range(T):
    n = int(input())
    # data 리스트를 n+4 크기로 설정
    data = [0] * (n+4)
    data[1] = 1
    data[2] = 2
    data[3] = 4

    # n이 4 이상인 경우
    # data[i] 값은 data[i-1]의 케이스에 1 더하는 경우 + data[i-2] 케이스에 2 더하는 경우 + data[i-3] 케이스에 3 더하는 경우 
    for i in range(4, n+1):
        data[i] = data[i-1] + data[i-2] + data[i-3]
    print(data[n])
