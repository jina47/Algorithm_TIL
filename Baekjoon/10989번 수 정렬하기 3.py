import sys

# 입력값 N
N = int(input())

# counting 리스트 만들기
counting = [0] * 10001

# counting[num] = num의 개수 를 만족하게 counting 업데이트
for i in range(N):
    num = int(sys.stdin.readline())
    counting[num] += 1

for i, cnt in enumerate(counting):
    # cnt가 1 이상이면 i를 cnt만큼 출력
    if cnt != 0:
        while cnt > 0:
            print(i)
            cnt -= 1
