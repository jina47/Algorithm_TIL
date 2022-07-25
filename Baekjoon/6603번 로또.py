### 1. combinations 라이브러리 이용
from itertools import combinations

while True:
    test = list(map(int, input().split()))
    k = test.pop(0)

    # 입력에 0이 들어오면 break
    if k == 0:
        break
    else:
        # 사전 순으로 출력하기 위해 sort
        test.sort()
        combi = combinations(test, 6)
        for ans in combi:
            print(' '.join(list(map(str, ans))))
        print('')
        
### 2. dfs 이용
def dfs(idx, depth, k):
    # combi 길이가 6이 되면 출력
    if depth == 6:
        print(' '.join(list(map(str, combi))))
        return
    
    else:
        # combi 인덱스(depth)에 담길 숫자 결정
        for i in range(idx, k):
            combi[depth] = test[i]
            # depth+1에 담길 숫자 결정
            dfs(i+1, depth+1, k)


# 출력할 숫자가 담긴 리스트 combi
combi = [0 for _ in range(6)]

# 입력
while True:
    test = list(map(int, input().split()))
    k = test.pop(0)

    # 입력에 0이 들어오면 break
    if k == 0:
        break
    else:
        # 사전 순으로 출력하기 위해 sort
        test.sort()
        dfs(0, 0, k)
        print('')