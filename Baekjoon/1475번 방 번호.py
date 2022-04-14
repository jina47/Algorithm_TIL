room = [int(i) for i in input()]
number = [0 for _ in range(10)]
for i in room:
    number[i] += 1
number[6] = (number[6] + number[9]) // 2 + (number[6] + number[9]) % 2
number[9] = number[6]
print(max(number))
