# 자연수 M의 각 자리수 + M = N일 떄, M은 N의 생성자
# N의 길이를 ln이라 지정
N = int(input())
ln = len(str(N))


# 생성자 M의 각 자리수의 합의 최댓값은 M의 길이에 9를 곱한 값
# M의 길이는 N의 길이와 같거나 하나 작은 값인데 최대의 경우만 생각하면 되므로 ln*9가 된다
# N에서 ln*9의 값을 빼준 값이 M으로 가능한 최소의 값이고 N에서 1을 빼준 값이 M으로 가능한 최대의 값이다
# M으로 가능한 수의 범위 중에서 num과 각 자리의 합이 N을 만족하는 경우 M이 되므로 가장 먼저 만족하는 때에 break해준다
# 만약 num이 N-1인데도 조건을 만족하지 못하면 0을 출력한다

for num in range(N-ln*9, N):
    # num은 0보다 커야 함
    if num <0:
        continue
    
    num_str = [int(s) for s in str(num)]
    if num + sum(num_str) == N:
        print(num)
        break

    if num == N-1:
        print(0)
