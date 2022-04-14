import sys

# 사람의 수
N = int(input())
# 시간을 리스트로 만들고 오름차순 정렬
times = list(map(int, sys.stdin.readline().split()))
times.sort()

# 현재 시간까지 더해준 값을 ans에 더해줌
ts, ans = 0, 0
for time in times:
    ts += time
    ans += ts

# 출력
print(ans)

