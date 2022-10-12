S = int(input())

sum = 0
for i in range(1, S):
    if i < S:
        S -= i
        sum += 1
    elif i == S:
        sum += 1
        break
    else:
        break
if S == 1:
    print(1)
else:
    print(sum)

