from collections import deque as dq

# 입력
N, M, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int ,input().split())))
number = list(map(int, input().split()))

A = dq(A)

# 1~6번 연산 함수 만들기 
def one(original):
    new_array = dq([])
    for _ in range(len(original)):
        new_array.append(original.pop())
    return new_array

def two(original):
    new_array = dq([])
    for i in range(len(original)):
        temp = original[i][::-1]
        new_array.append(temp)
    return new_array

def three(original):
    new_array = dq([[] for _ in range(len(original[0]))])
    for _ in range(len(original)):
        temp = original.pop()
        for i in range(len(temp)):
            new_array[i].append(temp[i])
    return new_array


def four(original):
    new_array = dq([[] for _ in range(len(original[0]))])
    for _ in range(len(original)):
        temp = original.popleft()
        for i in range(len(temp)):
            new_array[len(temp)-i-1].append(temp[i])
    return new_array    

def five(original):
    new_array = dq([[0 for _ in range(len(original[0]))] for _ in range(len(original))])
    row = len(original)
    col = len(original[0])
    for r in range(0, row//2):
        for c in range(0, col//2):
            new_array[r][c+col//2] = original[r][c]
    for r in range(0, row//2):
        for c in range(col//2, col):
            new_array[r+row//2][c] = original[r][c]
    for r in range(row//2, row):
        for c in range(col//2, col):
            new_array[r][c-col//2] = original[r][c]
    for r in range(row//2, row):
        for c in range(0, col//2):
            new_array[r-row//2][c] = original[r][c]
    return new_array
        
def six(original):
    new_array = dq([[0 for _ in range(len(original[0]))] for _ in range(len(original))])
    row = len(original)
    col = len(original[0])
    for r in range(0, row//2):
        for c in range(0, col//2):
            new_array[r+row//2][c] = original[r][c]
    for r in range(0, row//2):
        for c in range(col//2, col):
            new_array[r][c-col//2] = original[r][c]
    for r in range(row//2, row):
        for c in range(col//2, col):
            new_array[r-row//2][c] = original[r][c]
    for r in range(row//2, row):
        for c in range(0, col//2):
            new_array[r][c+col//2] = original[r][c]
    return new_array

# 연산 실행
for num in number:
    if num == 1:
        A = one(A)
    elif num == 2:
        A = two(A)
    elif num == 3:
        A = three(A)
    elif num == 4:
        A = four(A)
    elif num == 5:
        A = five(A)
    elif num == 6:
        A = six(A)

# 최종 배열 출력
for idx in range(len(A)):
    print(' '.join(map(str, A[idx])))