# 입력
heights = []
for _ in range(9):
    heights.append(int(input()))

# 9개 숫자를 7개 숫자로 조합을 만들어 합이 100이 되는 지 살펴보기
# 9개 숫자 중 2개를 골라서 전체 합에서 빼주었을 때 100이 되는지 구하기
def find100(total, heights):
    for i in range(9):
        for j in range(9):
            if i != j:
                minus = heights[i] + heights[j]
                if total-minus == 100:
                    return i, j

# 빼주어야하는 인덱스 i, j 찾기
total = sum(heights)
i, j = find100(total, heights)

# 합이 100이 되는 숫자들만 answer에 담기
answer = []
for number in heights:
    if number != heights[i] and number != heights[j]:
        answer.append(number)

# 출력
answer.sort()
for a in answer:
    print(a)