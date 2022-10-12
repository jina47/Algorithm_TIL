N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    visited = [0 for _ in range(26)]
    for c in word:
        if visited[ord(c)-97] == 0:
            temp = c
            visited[ord(c)-97] = 1
        elif c == temp:
            continue
        elif c != temp:
            break
    else:
        cnt += 1

print(cnt)