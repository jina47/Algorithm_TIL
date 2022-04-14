import heapq
N = int(input())
R = int(input())
students = list(map(int, input().split()))
que = []
# [추천수, 들어온 인덱스, 학생번호]로 배열을 만들어 힙 정렬
heapq.heappush(que, [1, 0, students[0]])
for i in range(1, R):
    # 사진틀이 남은 경우
    if len(que) < N:
        # 이미 학생번호가 있다면 추천수를 하나 올려줌
        for j in range(len(que)):
            if que[j][2] == students[i]:
                que[j][0] += 1
                heapq.heapify(que)
                break
        # 학생의 사진이 없으면 새로 넣어줌
        else:
            heapq.heappush(que, [1, i, students[i]])
    # 남는 사진틀이 없는 경우
    else:
        # 이미 학생 사진이 있는 경우 추천수를 올려줌
        for j in range(len(que)):
            if que[j][2] == students[i]:
                que[j][0] += 1
                heapq.heapify(que)
                break
        # 학생 사진이 없는 경우 제일 추천수가 적은 것, (추천수 적은 것이 2개 이상이면) 그 중 오래된 것을 빼주고 새로 넣어줌
        else:
            heapq.heappop(que)
            heapq.heappush(que, [1, i, students[i]])

# 학생번호 순으로 오름차순 정렬 후 출력
que.sort(key=lambda x: x[2])
for idx in range(len(que)):
    print(que[idx][2], end= ' ')
