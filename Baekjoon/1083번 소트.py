N = int(input())
lst = list(map(int, input().split()))
S = int(input())

# N이 1이거나 S가 0이라면 입력받은 원소들 그대로 출력
if N == 1 or S == 0:
    print(' '.join(map(str, lst)))
else:
    answer = []
    while S > 0:
        # 원소 교환을 꼭 S번 해야 하는 것이 아니므로 사전순으로 가장 뒷서게 되면 break 
        if lst == []:
            break
        # S가 lst 길이보다 크다면 lst에서 최댓값 찾기
        if S >= len(lst):
            idx = lst.index(max(lst))
            # 최댓값이 원하는대로 제일 앞에 위치하면 answer에 넣어주고 lst에서는 빼줌
            if idx == 0:
                answer.append(lst.pop(0))
                continue
            # 최댓값이 아직 앞으로 이동할 수 있는 경우 앞의 원소와 교환
            temp = lst[idx]
            lst[idx] = lst[idx-1]
            lst[idx-1] = temp
            S -= 1
        # S가 lst 길이보다 작다면 lst[:S+1]에서 최댓값 찾아서 앞으로 이동
        else:
            idx = lst.index(max(lst[:S+1]))
            if idx == 0:
                answer.append(lst.pop(0))
                continue
            temp = lst[idx]
            lst[idx] = lst[idx-1]
            lst[idx-1] = temp
            S -= 1
    # 교환 후 결과 출력
    print(' '.join(map(str, answer + lst)))
