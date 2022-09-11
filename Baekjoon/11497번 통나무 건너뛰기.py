T = int(input())
for _ in range(T):
    N = int(input())
    # 통나무 높이 순으로 오름차순 정렬
    L = list(map(int, input().split()))
    L.sort()
    answer = 0
    # 처음 통나무 기준 번갈아가며 양쪽에 통나무들을 세워서 원형 만들기 
    for i in range(N-2):
        # 통나무 높이 차의 최댓값을 answer로 저장
        if L[i+2] - L[i] > answer:
            answer = L[i+2] - L[i]
    print(answer)
        
