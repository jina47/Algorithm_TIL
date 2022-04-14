import sys
N = int(input())
A = [int(i) for i in sys.stdin.readline().split()]
A.sort()

M = int(input())
B = [int(i) for i in sys.stdin.readline().split()]

# 이분탐색
for i in range(M):
    left = 0
    right = N-1
    while True:
        mid = (left + right)//2
        if B[i] < A[mid]:
            right = mid - 1
        elif B[i] > A[mid]:
            left = mid + 1
        else:
            print(1)
            break

        if left >= right and B[i] != A[left]:
            print(0)
            break

            