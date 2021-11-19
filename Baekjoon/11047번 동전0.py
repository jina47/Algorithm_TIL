N, K = map(int, input().split())

# 동전의 가치 리스트로 만들기
values = [int(input()) for _ in range(N)]
# 오름차순으로 주어지므로 내림차순으로 바꿔줌
values.reverse()

# cnt로 동전 개수의 최솟값 구하기
cnt = 0
for v in values:
    # v가 K보다 크면 동전을 이용할 수 없으므로 continue
    if v > K:
        continue
    # v가 K보다 크면 동전을 최대로 몇개 이용할 수 있는지 cnt에 더해줌
    # K에는 동전의 개수와 가치를 더한 값을 뺴줌
    else:
        cnt += K//v
        K -= K//v * v

print(cnt)
