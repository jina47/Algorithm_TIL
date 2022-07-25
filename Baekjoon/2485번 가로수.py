from math import gcd

N = int(input())
trees = []
for _ in range(N):
    trees.append(int(input()))

# 가로수 간격의 최대공약수 찾아야 함
trees.sort()
interval = trees[1]-trees[0]
for i in range(2, N):
    if interval > gcd(interval, trees[i]-trees[i-1]):
        interval = gcd(interval, trees[i]-trees[i-1])

# interval만큼 세워야 하는 가로수 최소수
ans = 0
for i in range(1, N):
    ans += (trees[i]-trees[i-1]) // interval
# 출력
print(ans-N+1)
