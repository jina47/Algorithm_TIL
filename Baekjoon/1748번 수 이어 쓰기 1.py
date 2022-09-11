N = input()
length = len(N)

answer = 0
for i in range(1, length):
    answer += (10**i - 10**(i-1))*i
answer += (int(N) - 10**(length-1) + 1) * length
print(answer)