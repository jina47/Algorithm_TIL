N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 오름차순 정렬해준다
# B의 최댓값을 빼주면서 A와 차례로 곱해줌
A.sort()
S = 0
for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))
    
print(S)

