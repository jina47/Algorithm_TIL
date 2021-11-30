import sys
# 식 입력 후 '-' 기준으로 split
equation = sys.stdin.readline().strip().split('-')

# equation을 '+' 기준으로 split한 후 그 합을 다시 넣어줌
for i in range(len(equation)):
    equation[i] = sum(map(int, equation[i].split('+')))

# 첫 번째 숫자에서 뒤의 숫자들을 빼줌
answer = equation[0]
for j in range(1, len(equation)):
    answer -= equation[j]
print(answer)
    
