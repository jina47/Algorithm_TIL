from collections import deque as dq
import sys

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    p = sys.stdin.readline().strip() # 함수
    n = int(input()) # 배열 속 수의 개수
    s = sys.stdin.readline().strip() # 배열

    # s가 []라면 빈 배열, 아니라면 str의 형태이므로 deque형태로 만들어줌
    if s != '[]':
        arr = dq([int(i) for i in s[1:-1].split(',')])
    else:
        arr = []
    
    # 함수 명령어 중 R의 개수를 cnt로 판별
    cnt = 0
    for j in range(len(p)):
        if p[j] == 'R':
            cnt += 1
        
        elif p[j] == 'D':
            # arr가 비어있지 않을 때 cnt가 짝수라면 앞에서 수를 빼주고 cnt가 홀수라면 뒤에서 수를 빼줌
            if arr:
                if cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            # arr가 비어있으면 deque를 수행할 수 없으므로 error 출력
            else:
                print('error')
                break
        
        # break 되지 않고 끝까지 for문을 돌았을 때 arr 출력
        if j == len(p)-1:
            # cnt가 홀수라면 전체 배열을 한 번 뒤집어주면 됨
            if cnt % 2 == 1:
                arr.reverse()
            print('[' + ','.join(map(str,list(arr))) + ']')

