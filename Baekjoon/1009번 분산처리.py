T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        # a를 끝자리 수로 갱신
        a = a % 10
        # b는 4로 나눠준 나머지로 갱신
        b = b % 4
        if b == 0:
            print(a**4 % 10)
        else:
            print(a**b % 10)
