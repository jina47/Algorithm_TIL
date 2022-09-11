
while True:
    try:
        n = int(input())
    except:
        break
    i = 0
    answer = 0
    while True:
        answer += 10**i
        if answer % n == 0:
            print(i+1)
            break
        else:
            i += 1
