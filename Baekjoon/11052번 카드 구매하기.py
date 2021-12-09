N = int(input())
costs = list(map(int, input().split()))
costs = [0] + costs
for num in range(2, N+1):
    # num//2+num%2의 값부터 num-1까지 costs[num]과 num을 만들 수 있는 값을 인덱스로 갖는 costs값의 합 비교해서 최댓값 저장
    for idx in range(num//2+num%2, num):
        costs[num] = max(costs[num], costs[idx] + costs[num-idx])
print(costs[-1])
