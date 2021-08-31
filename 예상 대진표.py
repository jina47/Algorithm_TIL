def solution(N,A,B):
    while N != 1:
        n = min(A, B)
        m = max(A, B)
        if n <= N/2 and m > N/2:
            return len(bin(int(N))[2:])-1

        elif n > N/2 and m > N/2:
            A -= N/2
            B -= N/2
            N = N/2
        else:
            N = N/2