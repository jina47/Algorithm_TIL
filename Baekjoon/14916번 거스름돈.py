# 거스름돈 n
n = int(input())

coins = [0, 0, 1, 0, 0, 1]
if n > 5:
    coins += [0 for _ in range(6, n+1)]

# coins[i-2]와 coins[i-5]가 0이 아닐 때 coins[i] = min(coins[i-2], coins[i-5]) + 1
for i in range(3, n+1):
    if i < 5 and coins[i-2] != 0:
        coins[i] = coins[i-2] + 1
    else:
        if coins[i-2] != 0 and coins[i-5] != 0:
            coins[i] = min(coins[i-2], coins[i-5]) + 1
        elif coins[i-2] != 0 and coins[i-5] == 0:
            coins[i] = coins[i-2] + 1
        elif coins[i-5] != 0 and coins[i-2] == 0:
            coins[i] = coins[i-5] + 1

# coins[n] 출력 (0이면 -1 출력)
if coins[n] == 0:
    print(-1)
else:
    print(coins[n])
