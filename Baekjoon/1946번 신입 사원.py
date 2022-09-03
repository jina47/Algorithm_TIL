# 테스트 케이스
T = int(input())

for _ in range(T):
    # 지원자의 숫자
    N = int(input())
    # [서류 순위, 면접 순위] 을 담는 grade
    grade = []
    for _ in range(N):
        grade.append(list(map(int, input().split())))
    # 서류 순위 기준 오름차순 정렬
    grade.sort()

    # 선발 가능 신입사원의 인원 cnt (서류 성적 1등인 사람은 무조건 선발)
    cnt = 1
    # 서류 순위 1등인 사람의 면접 순위
    interview = grade[0][1]

    for i in range(1, N):
        # 현재 저장되어 있는 면접 순위보다 더 높은 순위여야 선발 가능 (interview 갱신)
        if interview > grade[i][1]:
            cnt += 1
            interview = grade[i][1]
    
    # 선발 가능 신입 사원 인원 출력
    print(cnt)


