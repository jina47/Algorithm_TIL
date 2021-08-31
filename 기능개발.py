def solution(progresses, speeds):
    days = []
    answer = [1]

    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            days.append(int((100-progresses[i])/speeds[i]))
        else:
            days.append(int((100-progresses[i])/speeds[i])+1)

    for j in range(len(days)-1):
        if days[j+1] <= max(days[:j+1]):
            answer[-1] += 1
        else:
            answer.append(1)
    return answer