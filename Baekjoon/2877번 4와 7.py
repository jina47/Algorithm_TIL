K = int(input())

# 이진수 이용
# K+1를 이진수로 표현했을 때 첫 자리를 제외하고 0은 4로 1은 7로 표기하면 됨
K += 1
answer = ''
while K > 1:
    a, b = K // 2, K % 2
    if b == 0:
        answer = '4' + answer
    elif b == 1:
        answer = '7' + answer
    K //= 2
print(answer)
