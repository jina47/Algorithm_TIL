# 수열의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))

lst = [[A[0]]]
for i in range(1, N):
    # lst를 요소의 길이가 긴 순서대로 나열
    # 길이가 같다면 마지막 값이 작은 순서대로 나열
    # 마지막 값도 같다면 처음 값이 작은 순서대로 나열
    lst.sort(key=lambda x: (-len(x), x[-1], x[0]))

    for l in lst:
        # lst는 길이가 긴 순서대로 나열되어 있으므로 l의 마지막 값보다 A[i]가 크면 l에 A[i]를 더해주고 그 리스트를 lst에 넣어주면서 break
        if l[-1] < A[i]:
            lst.append(l+[A[i]])
            break

    # 만약 for문을 다 돌았는데 A[i]가 최소값인 경우 lst에 [A[i]]를 추가
    if len(lst) == i:
        lst.append([A[i]])

# lst에서 길이가 가장 긴 요소의 길이를 출력
# 마지막 값을 더해주기 전까지 lst는 길이 순서대로 나열되어 있었으므로 lst[0]의 값이 가장 길이가 길 것임
# 마지막 값을 더해주고 길이 순으로 정렬하지 않았으므로 길이가 제일 긴 값은 lst[0]과 lst[-1]을 비교해보면 됨
# 배열이 더 긴 길이를 출력
print(len(max(lst[0], lst[-1])))
