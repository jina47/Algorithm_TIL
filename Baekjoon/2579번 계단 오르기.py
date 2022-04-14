import sys

# 계단의 개수 n
n = int(input())

# steps에 계단별 점수 저장
steps = [0]
for i in range(n):
    steps.append(int(sys.stdin.readline()))

# points 리스트로 최댓값 구하기
points = [[0, 0], [steps[1], 0]]

# points의 각 항은 2개의 요소로 되어있음
# 첫 번째 요소는 2칸 아래에서 올라오는 경우 : points[s-2]의 최댓값 + steps[s]
# 두 번째 요소는 1칸 아래에서 올라오는 경우 : points[s-1][0] + steps[s] 
for s in range(2, n+1):
    points.append([max(points[s-2]) + steps[s], points[s-1][0] + steps[s]])
    
print(max(points[-1]))