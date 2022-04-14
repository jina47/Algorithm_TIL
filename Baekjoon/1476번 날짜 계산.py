E, S, M = map(int, input().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
i = 0
while True:
    number = 28 * i + S
    if number!= 0 and number % 15 == E and number % 19 == M:
        print(number)
        break
    i += 1