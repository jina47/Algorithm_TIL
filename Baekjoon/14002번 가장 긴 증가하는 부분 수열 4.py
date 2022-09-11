# 입력
N = int(input())
A = list(map(int, input().split()))

# 증가하는 부분 담기
lst = [[] for _ in range(N)]
lst[0] = [A[0]]
for i in range(1, N):
    for j in range(i):
        # 증가하는 부분이면서 더 긴 수열 담기
        if A[i] > A[j]:
            if len(lst[i]) <= len(lst[j]):
                lst[i] = lst[j]
    lst[i] = lst[i] + [A[i]]

# 수열 길이 순서대로 정렬
lst.sort(key=lambda x: -len(x))
# 가장 긴 증가하는 부분 길이와 수열 출력
print(len(lst[0]))
print(' '.join(map(str, lst[0])))