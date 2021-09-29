def solution(N):
    ans = 0
    while N:
        if N % 2 != 0:
            ans += 1
            N = N-1
            if N == 0:
                break
        else:
            N = N/2

    return ans