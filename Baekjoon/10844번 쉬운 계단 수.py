# 입력값 N
N = int(input())

number = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# n번째 자리수에 올 수 있는 수의 개수는 2**(n-1)
# x로 시작했을 때 n번째 자리의 최댓값 = x + (n-1)
# x로 시작했을 때 n번째 자리의 최솟값 = x - (n-1) 
# x로 시작하는 경우 자릿수가 n일때 라고 생각해보자
# 자릿수가 n-1일 때 경우에 그 다음수로 넣을 수 있는 것들을 따져보기
# bottom-up방식으로 1 2 3 4 5 6 7 8 9로 시작
# 9개의 리스트로만 계속 해주면 되지 않을까...?!
for i in range(2, N+1):
    lst = []
    for num in number:
        if num-1 >= 0:
            lst.append(num-1)
        if num+1 <= 9:
            lst.append(num+1)
    number = lst
    print(number.count(0), number.count(9))
print(len(number) % 1000000000)
