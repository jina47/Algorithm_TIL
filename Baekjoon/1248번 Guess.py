import sys

# 입력
n = int(sys.stdin.readline())
signs = [s for s in sys.stdin.readline()]
# 이차원 형식으로 부등호 다시 배열
S = [[False for _ in range(n)] for _ in range(n)]
idx = 0
for i in range(n):
    for j in range(i, n):
        S[i][j] = signs[idx]
        idx += 1

# 재귀함수 작성
# 부등호 조건을 만족하는 배열 lst
# S의 각 행의 부등호 조건을 만족하는지 파악하기 위해 숫자들의 합을 담은 리스트 sumlst
def recur(lst, sumlst):
    # lst의 길이가 n+1이 되면 출력 후 시스템 종료
    if len(lst) == n+1:
        print(' '.join(map(str, lst[1:])))
        exit()

    # lst의 길이가 n+1보다 작으면 부등호 조건 만족하는 숫자 찾기
    for num in range(-10, 11):
        # 현재 lst의 길이를 기준으로 새로운 num이 들어왔을 때 조건 만족하는지 판별
        for i in range(len(lst)):
            # 부등호 조건을 만족하지 못하면 break
            if S[i][len(lst)-1] == '-':
                if sumlst[i] + num >= 0:
                    break
            elif S[i][len(lst)-1] == '+':
                if sumlst[i] + num <= 0:
                    break
            elif S[i][len(lst)-1] == '0':
                if sumlst[i] + num != 0:
                    break
        # 모든 부등호 조건을 만족하면 num을 넣은 새로운 new_lst와 새로운 합 num_sumlst를 입력값으로 하는 재귀 함수 실행
        else:
            new_sumlst = [s+num if i < len(lst) else s for i, s in enumerate(sumlst)]
            new_lst = lst + [num]
            recur(new_lst, new_sumlst)


recur([0], [0 for _ in range(n)])

