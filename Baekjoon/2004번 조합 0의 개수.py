n, m = map(int, input().split())

cnt = 0
# 이렇게 하면 시간초과이므로 거꾸로 5를 곱해줘서 더해주는 방식 이용해야함..
for num in range(1, n+1):
    if num == m+1:
        left = cnt
    if num == n-m+1 :
        right = cnt
    
    while num % 5 == 0:
        cnt += 1
        num //= 5

print(cnt-(left+right))


