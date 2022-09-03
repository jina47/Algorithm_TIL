# 입력
N, P = map(int, input().split())
fret = []
for _ in range(N):
    fret.append(list(map(int, input().split())))

# 각 기타 줄마다 누르고 있는 프렛 상태를 담는 stack
stack = [[] for _ in range(7)]
# 손가락 움직이는 횟수를 구하는 cnt
cnt = 0
# 손가락 움직이는 횟수 구하기
for i, f in fret:
    # 해당 줄에 아직 누르고 있는 프렛이 없으면 프렛을 누름
    if stack[i] == []:
        stack[i].append(f)
        cnt += 1
    # 해당 줄에 누르고 있는 프렛이 있는 경우
    else:
        # 누르고 있는 프렛보다 눌러야 하는 프렛이 더 높은 경우 프렛 누르기
        if stack[i][-1] < f:
            cnt += 1
            stack[i].append(f)
        # 누르고 있는 프렛보다 눌러야 하는 프렛이 더 낮은 경우 손가락 떼기
        elif stack[i][-1] > f:
            while stack[i][-1] > f:
                stack[i].pop()
                cnt += 1
                # 손가락을 다 뗀 경우 눌러야 하는 프렛 f 누르기
                if stack[i] == []:
                    stack[i].append(f)
                    cnt += 1
                    break
                if stack[i][-1] < f:
                    stack[i].append(f)
                    cnt += 1
                    break
                elif stack[i][-1] == f:
                    break

# cnt 출력
print(cnt)
