def solution(weights, head2head):
    player = [[0,0,0,0] for _ in range(len(weights))] # 승률, 더 큰 무게 이긴 횟수, 몸무게, -(번호) 순으로(우선순위를 판단하는 순서) 정렬
    for i, h in enumerate(head2head):
        if h.count('W')+h.count('L') != 0: # 싸운 적 있는 경우, 승률 = 이긴 횟수/싸운 횟수
            player[i][0] = h.count('W')/(h.count('W')+h.count('L'))
        else: # 싸운 전적이 없는 경우 승률 = 0
            player[i][0] = 0 
        for j, d in enumerate(h): # 자신 무게보다 더 큰 무게의 복서를 이긴 횟수
            if d == 'W' and weights[i] < weights[j]:
                player[i][1] += 1
        player[i][2] = weights[i] # 본인의 몸무게
        player[i][3] = -(i+1) # 본인 번호의 음수
    
    player.sort(reverse=True) # 전체 내림차순 정렬
    answer = []
    for p in player:
        answer.append(-p[-1]) # 원래 번호를 answer에 append
    return answer