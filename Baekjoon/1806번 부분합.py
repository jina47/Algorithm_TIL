N, S = map(int, input().split())
arr = list(map(int, input().split()))

# end는 0, 부분합은 partial, 부분합의 길이는 cnt로 설정
end = 0
partial = 0
cnt = 100000

for start in range(N):
    # 부분합이 S보다 작고 end가 N보다 작으면 부분합에 arr[end]를 넣어주고 end += 1
    while partial < S and end < N:
        partial += arr[end]
        end += 1
    # 만약 부분합 partial이 S 이상이라면 현재 부분합의 길이가 cnt보다 작으면 cnt 새로 지정
    if partial >= S:
        if cnt > end-start:
            cnt = end-start
    # 그 다음 start에 대해 판단하기 위해 부분합에서 arr[start] 뺴줌
    partial -= arr[start]

# cnt가 100000이라면 부분합이 S이상인 구간이 없는 것이므로 0 출력
if cnt == 100000:
    print(0)
# 만약 cnt가 0이라면 start=end인 arr의 숫자가 S보다 큰 것이므로 길이는 1
elif cnt == 0:
    print(1)
# cnt 출력
else:
    print(cnt)