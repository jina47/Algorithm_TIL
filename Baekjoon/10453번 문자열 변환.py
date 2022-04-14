T = int(input())
for _ in range(T):
    A, B = map(str, input().strip().split())
    if len(A) != len(B) or A.count('a') != B.count('a') or A.count('b') != B.count('b'):
        print(-1)
    else:
        cnt = 0
        # A의 a인덱스를 start에 담고 B의 a인덱스를 end에 담음
        start, end = [], []
        for i in range(len(A)):
            if A[i] == 'a':
                start.append(i)
            if B[i] == 'a':
                end.append(i)
        # start와 end를 비교해서 같은 인덱스의 값이 다르면 그 값의 차이만큼 cnt에 더해줌
        for j in range(len(start)):
            if start[j] != end[j]:
                cnt += abs(end[j]-start[j])
        print(cnt)

