# 피보나치함수로 출력하게 되는 0의 개수와 1의 개수를 담는 배열 생성
def zeroone(N):
    # [0을 출력하는 수, 1을 출력하는 수]로 리스트 생성
    zero_one = [[1,0], [0,1]]

    if N == 0:
        return zero_one[0]

    elif N == 1:
        return zero_one[1]
    
    # 입력값 N이 2 이상일 때, zero_one[N]을 구하기 위해 리스트에 요소를 추가
    else:
        for i in range(2, N+1):
            zero_one.append([zero_one[i-1][0] + zero_one[i-2][0], zero_one[i-1][1] + zero_one[i-2][1]])
        return zero_one[N]


# 테스트 케이스 개수 T
T = int(input())

# 출력
for _ in range(T):
    N = int(input())
    print(' '.join(map(str, zeroone(N)))) 
