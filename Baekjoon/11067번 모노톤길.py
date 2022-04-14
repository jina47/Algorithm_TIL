T = int(input())
for _ in range(T):
    n = int(input())
    cafe = [[] for _ in range(100002)]
    
    # x좌표에 해당하는 배열에 [x, y]좌표를 넣어줌
    for _ in range(n):
        x, y = map(int, input().split())
        cafe[x].append([x, y])
    
    # x좌표를 기준으로 카페가 존재하는 전 x좌표의 끝 값의 y좌표를 target으로 설정
    target = 0
    for i in range(100002):
        if cafe[i] == []:
            continue
        else:
            # target과 y좌표 사이의 거리가 짧은 순서대로 cafe[x] 정렬
            cafe[i].sort(key=lambda x : abs(x[1]-target))
            # 정렬 후 cafe[x]의 끝에 존재하는 좌표의 y값을 target으로 재설정
            target = cafe[i][-1][1]
    
    # 카페를 순서대로 배열에 넣어줌
    # 인덱스+1 의 값이 카페의 번호
    answer = []
    for i in range(100002):
        if cafe[i] == []:
            continue
        else:
            answer += cafe[i]
    
    # 번호에 해당하는 카페 좌표 출력
    output = list(map(int, input().split()))
    for p in output[1:]:
        print(' '.join(map(str, answer[p-1])))
