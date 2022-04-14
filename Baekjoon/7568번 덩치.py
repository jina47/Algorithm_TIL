# 전체 사람의 수 N
N = int(input())

# [몸무게, 키]를 담을 리스트 생성
data = []

# data에 [몸무게, 키] 담기
for _ in range(N):
    x, y = map(int, input().split())
    data.append([x,y])

# 등수를 return하기 위한 rank_lst 리스트 생성
rank_lst = []

# 등수를 구하기 위한 탐색
for [x, y] in data:
    rank = 1
    for i in range(N):
        if x < data[i][0] and y < data[i][1]:
            rank += 1
    rank_lst.append(rank)

# 공백문자로 분리하여 출력
print(' '.join(map(str, rank_lst)))