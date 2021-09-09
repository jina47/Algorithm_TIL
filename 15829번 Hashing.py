n = int(input())
data = [ord(i)-96 for i in input()] # 소문자이므로 아스키코드에서 96을 빼면 원하는 정수값
answer = 0
for e,d in enumerate(data):
    answer += d * (31 ** e)
print(answer % 1234567891)