# 정수 K
K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
if stack:
    print(sum(stack))
else:
    print(0)