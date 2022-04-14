import math

# 테스트 케이스 개수 T
T = int(input())

for _ in range(T):
    # 두 자연수 A, B
    A, B = map(int, input().split())

    # 최소공배수 출력
    print(A*B//math.gcd(A, B))