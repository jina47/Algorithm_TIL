# 입력값 n
n = int(input())

# 피보나치 수를 담는 리스트 만들기
fibo = [0, 1]

# n이 1이면, 1 출력
if n == 1:
    print(1)
    
# n이 2 이상이면, 피보나치 수를 fibo에 담아서 마지막 값 출력
else:
    for i in range(2, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    print(fibo[-1])
