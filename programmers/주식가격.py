def solution(prices):
    # answer 길이가 prices 길이와 같으므로 0의 배열로 만들어줌
    answer = [0] * len(prices) 

    # prices의 맨 끝 값은 항상 0초 동안 가격이 떨어지지 않음
    # answer의 맨 끝 값이 0이므로 prices[-2]까지만 판단을 하면 됨
    for i in range(len(prices)-1):

        # prices[i]에 대해서 i번째 이후 값에 대해서만 탐색
        for j in range(i, len(prices)-1):

            # prices[i]보다 작은 prices[j]값이 있다면 가격이 떨어진 것이므로 break
            if prices[i] > prices[j]:
                break

            # prices[i]보다 prices[j]값이 크거나 같으면 가격이 떨어지지 않았으므로 1초를 더해줌
            else:
                answer[i] +=1

    return answer
