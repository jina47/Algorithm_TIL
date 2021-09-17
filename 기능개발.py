def solution(progresses, speeds):
    release = 0
    answer = []

    for i in range(len(progresses)):
        # 작업 기간을 day라고 정의
        # 100%에서 완료된 작업률만큼 빼주고 하루에 가능한 작업률로 나눠서 day를 구함

        # 나누어 떨어지면 day는 몫을 그대로 정의
        if (100-progresses[i]) % speeds[i] == 0:
            day = (100-progresses[i])//speeds[i]
        
        # 나누어 떨어지지 않으면 day는 (몫+1)로 정의
        else:
            day = (100-progresses[i])//speeds[i]+1
        
        # release보다 day가 크면 새로운 날에 기능이 배포되는 것이므로 answer에 새로운 1 추가
        # release는 day로 새롭게 정의
        if release < day :
            answer.append(1)
            release = day
            
        # release보다 day가 작거나 같으면 release에 같이 기능이 배포되는 것이므로 answer[-1]에 1 추가
        else:
            answer[-1] += 1
    
    return answer