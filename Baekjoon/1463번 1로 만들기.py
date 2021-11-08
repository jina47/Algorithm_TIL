# 입력 숫자 N
N = int(input())

cnt = [0] * (N+3)
# 1은 그 자체로 1이므로 연산을 하지 않아도 된다(cnt[1]=1)
# 2는 2로 나누어주면, 3은 3으로 나누어주면 1이 된다 따라서 연산은 한 번만 하면 된다
cnt[2] = 1
cnt[3] = 1

# N이 4 이상인 경우 
for i in range(4, N+1):
    # i가 6으로 나누어지는 경우 cnt[i//3], cnt[i//2], cnt[i-1] 중 최솟값에 1을 더해줌
    if i % 6 == 0:
        cnt[i] = min(cnt[i//3], cnt[i//2], cnt[i-1] ) + 1
    # i가 6의 배수는 아닌데 3의 배수인 경우 cnt[i//3], cnt[i-1] 중 더 작은 수에 1을 더해줌
    elif i % 3 == 0:
        cnt[i] = min(cnt[i-1], cnt[i//3]) + 1
    # i가 6의 배수는 아닌데 2의 배수인 경우 cnt[i//2], cnt[i-1] 중 더 작은 수에 1을 더해줌
    elif i % 2 == 0:
        cnt[i] = min(cnt[i-1], cnt[i//2]) + 1
    # 2의 배수도 아니고 3의 배수도 아닌 경우 cnt[i-1]의 값에 1을 더해줌
    else:
        cnt[i] = cnt[i-1] + 1

# cnt[N] 출력
print(cnt[N])
