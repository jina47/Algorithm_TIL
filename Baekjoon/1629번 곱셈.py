A, B, C = map(int, input().split())

def solve(A, B, C):
    # B가 1이면 A를 C로 나눈 나머지 return
    if B == 1:
        return A%C
    
    # B가 2 이상일 때 거듭제곱 이용
    # 짝수면 A에 B//2 만큼 곱한 숫자에 대한 나머지를 구해 제곱한 후 다시 C로 나눈 나머지 return
    if B % 2 == 0:
        B //= 2
        return solve(A, B, C)**2 % C
    # 홀수면 A에 B//2 만큼 곱한 숫자에 대한 나머지에 제곱한 뒤 A를 곱한 후 다시 C로 나눈 나머지 return
    else:
        B //= 2
        return (solve(A, B, C)**2)*A % C

# 출력
print(solve(A, B, C))