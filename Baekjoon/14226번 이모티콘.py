from collections import deque as dq

# 입력
S = int(input())

# 방문 여부 및 시간을 담는 리스트
second = [[0 for _ in range(2*S)] for _ in range(2*S)]

# 화면, 클립보드 순서대로 가지고 있는 이모티콘의 개수를 리스트에 담음
que = dq([[1, 0]])
# bfs로 최소 시간 탐색
while que:
    display, clipboard = que.popleft()
    
    # 화면에 있는 이모티콘의 개수가 S일 때 시간 출력 후 break
    if display == S:
        print(second[display][clipboard])
        break
    
    # 복사, 붙여넣기, 삭제 하는 경우
    for step in [0, clipboard, -1]:
        # 연산 후 화면의 이모티콘 갯수 nd
        nd = display + step
        
        # 복사 하는 경우 클립보드는 덮어쓰기가 되므로 display과 같은 개수를 가짐
        if step == 0:
            # display, clipboard의 이모티콘 개수를 판단하지 않은 경우만 que에 append
            if 0 <= display < 2*S and second[display][display] == 0:
                # 모든 연산은 1초가 걸림
                second[display][display] = second[display][clipboard] + 1
                que.append([display, display])
        
        # 붙여넣기나 삭제하는 경우 클립보드의 이모티콘 개수는 변동 없음
        else:
            # display, clipboard의 이모티콘 개수를 판단하지 않은 경우만 que에 append
            if 0 <= nd < 2*S and second[nd][clipboard] == 0:
                # 모든 연산은 1초가 걸림
                second[nd][clipboard] = second[display][clipboard] + 1
                que.append([nd, clipboard])