# 입력값 n
n = int(input())

# 수열 리스트 num
num = [int(input()) for _ in range(n)]

stack = []
ans = []
i, j = 0, 1
for j in range(1, n+1):
    stack.append(j)
    ans.append('+')

    while stack and stack[-1] == num[i]:
        ans.append('-')
        stack.pop()
        i += 1

if stack:
    print('NO')
else:
    for a in ans:
        print(a)
    
