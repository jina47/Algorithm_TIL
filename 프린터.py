def solution(priorities, location):
    answer = []
    ip = [[i, p] for i, p in enumerate(priorities)] # [인덱스, 우선순위값] 리스트 생성
    
    while len(answer) != len(priorities): # answer 리스트에 우선순위에 따라 출력하는 순서대로 ip값 넣어줌
        if ip[0][1] < max([i[1] for i in ip]): # 우선순위가 최대가 아니라면 후순위
            ip.append(ip[0])
            ip.pop(0)
        else: # 우선순위가 최대값이라면 answer값에 ip값을 넣어주고 ip에서는 제거
            answer.append(ip[0])
            ip.pop(0)
            if answer[-1][0] == location: # answer에 넣어준 값의 첫 번째 요소가 location 값과 같으면 len(answer)가 인쇄되는 차례이므로 return
                return len(answer)