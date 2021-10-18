def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        # 직사각형의 넓이만 구하면 되므로 [가로, 세로]의 값 중 큰 값을 a, 작은 값을 b로 설정
        a = max(size[0], size[1])
        b = min(size[0], size[1])
        
        # w보다 a가 크면 w를 a로 정의, h보다 b가 크면 h를 b로 정의
        if w < a:
            w = a
        if h < b:
            h = b

    # for문을 다 돌면 w는 각 직사각형의 큰 값들 중 가장 큰 값, h는 직사각형의 작은 값들 중 가장 큰 값을 가짐
    # w와 h의 곱을 답으로 return
    return w*h
